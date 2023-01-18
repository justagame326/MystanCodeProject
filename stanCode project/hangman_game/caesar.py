"""
File: caesar.py
Name: Jerry
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program is to decipher
    """
    decipher()


def decipher():
    n = int(input("Secret number: "))
    s = input("What's the ciphered string? ")
    s = upper(s)
    ans = ""
    for i in range(len(s)):
        ch = s[i]
        b = ALPHABET.find(s[i])
        if b+n >= 26:
            b -= 26
            ans += ALPHABET[b+n]
        elif b == -1:
            ans += ch
        else:
            ans += ALPHABET[b+n]
    print("The deciphered string is: " + ans)


def upper(s):
    ans = ""
    for i in range(len(s)):
        ch = s[i]
        b = ALPHABET.find(s[i])
        if ch.islower():
            ans += ch.upper()
        elif ch.isupper():
            ans += ch
        elif b == -1:
            ans += ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
