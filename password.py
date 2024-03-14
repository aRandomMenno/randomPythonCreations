
import random

def password(length):
    # & List with possible characters & symbols.
    pwChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'm', '@', '#', '€', '_', '&', '-', '+', '(', ')', '/', '*', '"', ':', ';', '!', '?', ',', '.', '~', '`', '|', '£', '¥', '$', '¢', '^', '°', '=', '{', '}', '\\', '%', '[', ']', '<', '>']        # & print 1 character for length.
    password = ''
    for a in range(0, length+1):
        password += (random.choice(pwChars))
    return password

length = int(input('Choose a password length: '))
print(password(length))