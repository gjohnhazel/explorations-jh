# ASCII Art for 'Hello, World!'

ascii_art = {
    'H': 'H',
    'e': 'e',
    'l': 'l',
    'o': 'o',
    ',': ',',
    ' ': ' ',
    'W': 'W',
    'r': 'r',
    'd': 'd',
    '!' : '!'
}

for letter in 'Hello, World!':
    print(ascii_art.get(letter, '?'))  # Using '?' as the default value for missing keys
