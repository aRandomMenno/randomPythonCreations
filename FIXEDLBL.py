
encryptStr = 'can you decrypt me 1234567890'
decryptStr = '992.928.291.741.497.844.810.741.370.365.992.312.497.694.274.741.477.365.741.289.610.83.450.953.687.288.194.547.522.'

def encrypt(a) -> str:
    letterToNum = {
        'a': '928.', 'b': '911.', 'c': '992.', 'd': '370.', 'e': '365.',
        'f': '188.', 'g': '614.', 'h': '847.', 'i': '62.', 'j': '675.',
        'k': '934.', 'l': '97.', 'm': '477.', 'n': '291.', 'o': '844.',
        'p': '694.', 'q': '383.', 'r': '312.', 's': '156.', 't': '274.',
        'u': '810.', 'v': '319.', 'w': '24.', 'x': '626.', 'y': '497.',
        'z': '253.', ' ': '741.', '1': '289.', '2': '610.', '3': '83.', 
        '4': '450.', '5': '953.', '6': '687.', '7': '288.', '8': '194.', 
        '9': '547.', '0': '522.'
    }
    encryptedStr = ''
    for letter in a:
        encryptedStr += letterToNum.get(letter, '')
    return encryptedStr

def decrypt(encryptedStr) -> str:
    numToLetter = {
        '928': 'a', '911': 'b', '992': 'c', '370': 'd', '365': 'e',
        '188': 'f', '614': 'g', '847': 'h', '62': 'i', '675': 'j',
        '934': 'k', '97': 'l', '477': 'm', '291': 'n', '844': 'o',
        '694': 'p', '383': 'q', '312': 'r', '156': 's', '274': 't',
        '810': 'u', '319': 'v', '24': 'w', '626': 'x', '497': 'y',
        '253': 'z', '741': ' ', '289': '1', '610': '2', '83': '3', 
        '450': '4', '953': '5', '687': '6', '288': '7', '194': '8', 
        '547': '9', '522': '0'
    }
    decrypted = ''
    test = encryptedStr.rstrip('.').split('.')
    print(*test, sep=', ')
    for num in test:
        if num in numToLetter:
            decrypted += numToLetter[num]
        else:
            print(f"Invalid code: {num}")
    return decrypted

if __name__ == '__main__':
    print(encrypt(encryptStr))
    print(decrypt(decryptStr))
