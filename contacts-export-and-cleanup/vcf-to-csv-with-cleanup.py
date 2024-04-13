import csv
import vobject

def vcard_to_csv_with_filters(vcf_path, csv_path, filters):
    # Parse the VCF contents
    with open(vcf_path, 'r') as vcf_file:
        vcards = vobject.readComponents(vcf_file.read())

    # Define the CSV headers
    csv_headers = ['first_name', 'last_name', 'display_name', 'company', 'email', 'telephone']
    
    # Open the CSV file for writing
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()

        # Iterate over each vCard and extract information
        for vcard in vcards:
            contact_info = extract_contact_info(vcard, csv_headers)

            # Apply filters
            if not passes_filters(contact_info, filters):
                continue

            # Write the contact info to the CSV file
            writer.writerow(contact_info)

def extract_contact_info(vcard, csv_headers):
    """Extracts contact information from a vCard."""
    contact_info = {header: '' for header in csv_headers}
    names = vcard.n.value if hasattr(vcard, 'n') else None
    contact_info['first_name'] = names.given if names else ''
    contact_info['last_name'] = names.family if names else ''
    contact_info['display_name'] = vcard.fn.value if hasattr(vcard, 'fn') else ''
    contact_info['email'] = vcard.email.value if hasattr(vcard, 'email') else ''
    contact_info['telephone'] = vcard.tel.value if hasattr(vcard, 'tel') else ''
    contact_info['company'] = vcard.org.value[0] if hasattr(vcard, 'org') else ''
    return contact_info

def passes_filters(contact_info, filters):
    """Checks if a contact passes all filtering criteria."""
    # Check for empty first name
    if not contact_info['first_name'].strip():
        return False
    # Check for blank email address
    if not contact_info['email'].strip():
        return False
    # Domain and search term filtering
    if contact_info['email'].split('@')[-1] in filters['domains_to_remove']:
        return False
    if any(term in contact_info.values() for term in filters['search_terms_to_remove']):
        return False
    return True


# Filters setup
filters = {
    'domains_to_remove': [''],
    'search_terms_to_remove': [''],
}

# Define the input VCF and output CSV file paths
vcf_file_path = 'contacts.vcf'
csv_file_path = 'contacts-export.csv'

# Process the VCF, convert to CSV, and apply filters
vcard_to_csv_with_filters(vcf_file_path, csv_file_path, filters)

print(f'VCF to CSV conversion and filtering completed. CSV file saved as {csv_file_path}.')
