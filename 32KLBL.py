
# ! IMPORTANT NOTICE: THERE IS A POSSIBILITY THAT IN SOME CASES A TWO LETTERS WILL ROLL THE SAME NUMBER IN THIS CASE `PART` OF THE ENCRYPTED MESSAGE MAY NOT BE RECOVERABLE!!!

import random

encryptStr = '<enter something>'
decryptStr = '3416.7634.10845.15924.7634.7843.24192.23788.30568.16011.7634.15924.17931.16747.10845.4484.24440.'
encryptKey = 'super secret key'
decryptKey = 'super secret key'


def RN0(key, symbol) -> str:
    random.seed(key + symbol)
    tmp = str(random.randint(0, 32768))
    tmp += '.'
    return tmp

def RN1(key, symbol) -> str:
    random.seed(key + symbol)
    tmp = str(random.randint(0, 32768))
    return tmp

def encrypt(encryptStr, key) -> str:
    encryptStr = encryptStr.lower()
    letterToNum = {
        'a': RN0(key, 'a'), 'b': RN0(key, 'b'), 'c': RN0(key, 'c'), 'd': RN0(key, 'd'), 'e': RN0(key, 'e'),
        'f': RN0(key, 'f'), 'g': RN0(key, 'g'), 'h': RN0(key, 'h'), 'i': RN0(key, 'i'), 'j': RN0(key, 'j'),
        'k': RN0(key, 'k'), 'l': RN0(key, 'l'), 'm': RN0(key, 'm'), 'n': RN0(key, 'n'), 'o': RN0(key, 'o'),
        'p': RN0(key, 'p'), 'q': RN0(key, 'q'), 'r': RN0(key, 'r'), 's': RN0(key, 's'), 't': RN0(key, 't'),
        'u': RN0(key, 'u'), 'v': RN0(key, 'v'), 'w': RN0(key, 'w'), 'x': RN0(key, 'x'), 'y': RN0(key, 'y'),
        'z': RN0(key, 'z'), '1': RN0(key, '1'), '2': RN0(key, '2'), '3': RN0(key, '3'), '4': RN0(key, '4'), 
        '5': RN0(key, '5'), '6': RN0(key, '6'), '7': RN0(key, '7'), '8': RN0(key, '8'), '9': RN0(key, '9'), 
        '0': RN0(key, '0'), ' ': RN0(key, '/'), '?': RN0(key, '?'), '!': RN0(key, '!'), '<': RN0(key, '<'),
        '>': RN0(key, '>'), ',': RN0(key, ','), '.': RN0(key, '.'), ':': RN0(key, ':')
    }
    encryptedStr = ''
    for letter in encryptStr:
        encryptedStr += letterToNum.get(letter, '')
    return encryptedStr

def decrypt(encryptedStr, key) -> str:
    numToLetter = {
        RN1(key, 'a'): 'a', RN1(key, 'b'): 'b', RN1(key, 'c'): 'c', RN1(key, 'd'): 'd', RN1(key, 'e'): 'e',
        RN1(key, 'f'): 'f', RN1(key, 'g'): 'g', RN1(key, 'h'): 'h', RN1(key, 'i'): 'i', RN1(key, 'j'): 'j',
        RN1(key, 'k'): 'k', RN1(key, 'l'): 'l', RN1(key, 'm'): 'm', RN1(key, 'n'): 'n', RN1(key, 'o'): 'o',
        RN1(key, 'p'): 'p', RN1(key, 'q'): 'q', RN1(key, 'r'): 'r', RN1(key, 's'): 's', RN1(key, 't'): 't',
        RN1(key, 'u'): 'u', RN1(key, 'v'): 'v', RN1(key, 'w'): 'w', RN1(key, 'x'): 'x', RN1(key, 'y'): 'y',
        RN1(key, 'z'): 'z', RN1(key, '1'): '1', RN1(key, '2'): '2', RN1(key, '3'): '3', RN1(key, '4'): '4',
        RN1(key, '5'): '5', RN1(key, '6'): '6', RN1(key, '7'): '7', RN1(key, '8'): '8', RN1(key, '9'): '9',
        RN1(key, '0'): '0', RN1(key, '/'): ' ', RN1(key, '?'): '?', RN1(key, '!'): '!', RN1(key, '<'): '<',
        RN1(key, '>'): '>', RN1(key, ','): ',', RN1(key, '.'): '.', RN1(key, ':'): ':'
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
    print(encrypt(encryptStr, encryptKey))
    print(decrypt(decryptStr, decryptKey))
