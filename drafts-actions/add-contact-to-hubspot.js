// HubSpot API key
const apiKey = 'API_KEY_HERE';

// Sample draft content as a string variable
const sampleDraftContent = `
Sample Contact
example.com
example@example.com
`;

// Regular Expressions for email, phone, and URL
const emailRegex = /[\w.-]+@[\w.-]+\.\w+/;
const phoneRegex = /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/;
const urlRegex = /https?:\/\/\S+/;

// Function to parse draft content
function parseDraft(content) {
    let contact = {
        notes: ''
    };

    const lines = content.split('\n').filter(line => line.trim() !== '');
    contact.name = lines[0]; // First line is name

    lines.slice(1).forEach(line => {
        if (emailRegex.test(line)) {
            contact.email = line.match(emailRegex)[0];
        } else if (phoneRegex.test(line)) {
            contact.phone = line.match(phoneRegex)[0];
        } else if (urlRegex.test(line)) {
            contact.url = line.match(urlRegex)[0];
        } else {
            contact.notes += line + '\n'; // Adds other lines to notes
        }
    });

    return contact;
}

// Function to create contact in HubSpot
async function createContactInHubSpot(contact) {
    const url = 'https://api.hubapi.com/crm/v3/objects/contacts';
    const headers = {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
    };
    const body = JSON.stringify({
        properties: {
            firstname: contact.name, // Assumes name is first name
            email: contact.email,
            phone: contact.phone,
            website: contact.url,
            hs_content_membership_notes: contact.notes
            // Add more properties as needed
        }
    });

    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: body
    });

    return response.json();
}

// Main execution
(async () => {
    try {
        const contact = parseDraft(sampleDraftContent);
        const response = await createContactInHubSpot(contact);
        console.log('HubSpot API Response:', response);
    } catch (error) {
        console.error('Error:', error);
    }
})();

// Note: `fetch` needs to be available in your testing environment.
// If not, consider using `node-fetch` or a similar library in Node.js.
