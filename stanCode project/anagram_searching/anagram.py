"""
File: anagram.py
Name: Jerry
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program is to fina all anagrams of the word user input
    """
    lst = read_dictionary()
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        s = input("Find anagrams for: ")
        start = time.time()
        dic = []  # use to collect same length word
        for word in lst:
            if len(word) == len(s):
                dic.append(word)
        if s == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(s, dic)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, "r") as f:
        lst = []
        for line in f:
            lst.append(line.strip())
    return lst


def find_anagrams(s, dic):
    """
    :param s: (str) the word user input
    :return: (list) the list of all anagrams
    """
    anagrams = []
    length_of_s = len(s)
    find_anagrams_helper(s, dic, "", length_of_s, anagrams)
    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, dic, current_s, length_of_s, anagrams):
    if len(current_s) == length_of_s:
        if current_s in dic and current_s not in anagrams:
            print(f'Found: {current_s}')
            print("Searching...")
            anagrams.append(current_s)
    else:
        for ch in s:
            # Choose
            current_s += ch
            s = re_new(s, ch)
            # Explore
            if (length_of_s)-2 > len(current_s) > 1:
                if has_prefix(current_s, dic):
                    find_anagrams_helper(s, dic, current_s, length_of_s, anagrams)
            else:
                find_anagrams_helper(s, dic, current_s, length_of_s, anagrams)
            # Un-choose
            s += current_s[len(current_s) - 1:]
            current_s = current_s[:-1]


def re_new(string, ch):
    new_s = ''
    for i in range(len(string)):
        alpha = string[i]
        if i == string.find(ch):
            new_s += ""
        else:
            new_s += alpha
    return new_s


def has_prefix(sub_s, dic):
    """
    :param sub_s: (str) sub_string of current_s that would be search if same opening sub-string of word in the dictionary
    :return: True or False
    """
    for word in dic:
        if word[0] == sub_s[0]:  # Only compared with same first alphabet words
            if word.startswith(sub_s):
                return True
    return False


if __name__ == '__main__':
    main()
