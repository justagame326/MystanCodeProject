"""
File: name_sq.py (extension)
Name: Jerry
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    This program prints a name in a square pattern!
    """
    print("This program prints a name in a square pattern!")
    s = input("Name: ")
    for i in range(len(s)):
        ans = ""
        for j in range(len(s)):
            if i == 0:
                ch = s[i + j]
                ans += ch
            if 0 < i < len(s)-1:
                if i+j >= len(s):
                    i -= len(s)
                ch = s[i + j]
                if j == 0:
                    ans += ch
                elif 0 < j < len(s)-1:
                    ans += " "
                elif j == len(s)-1:
                    i += len(s)
                    ch1 = s[j-i]
                    ans += ch1
            if i < 0:
                i += len(s)
            if i == len(s)-1:
                ch2 = s[i-j]
                ans += ch2
        print(ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
