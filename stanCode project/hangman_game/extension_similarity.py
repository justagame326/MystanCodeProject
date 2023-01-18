"""
File: similarity.py (extension)
Name: Jerry
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program finds DNA similarity
    """
    d = input("Please give me a DNA sequence to search: ")
    s = input("What DNA sequence would you like to match? ")
    n = len(d) - len(s) + 1  # n means how many times to compare
    d = upper(d)  # d = d.upper()
    s = upper(s)  # s = s.upper()
    r = 0  # r means same alphabet ratio, start from 0
    m = ""  # m means the best match sequence of d, start from ""
    for i in range(n):
        b = 0  # b means same alphabet count between d & s, start from 0
        for j in range(len(s)):
            ch = s[j]
            ch1 = d[j+i]
            if ch == ch1:
                b += 1
        r1 = b / len(s)
        if r1 > r:
            r = r1
            m = d[i:i+len(s)]
    print("The best match is " + m)


def upper(d):
    ans = ""
    for i in range(len(d)):
        ch = d[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
