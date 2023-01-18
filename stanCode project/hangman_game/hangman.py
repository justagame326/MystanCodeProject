"""
File: hangman.py
Name: Jerry
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman!
    """
    ans = random_word()
    print("The word looks like ", end="")
    for i in range(len(ans)):
        print("_", end="")
    print("")
    n = N_TURNS
    print("You have " + str(n) + " wrong guesses left.")
    p = ""
    for i in range(len(ans)):
        ch = ans[i]
        if ch.isalpha:
            p += "_"  # p means all _ for each alphabet of ans (before guessing)
    while True:
        guess = ""
        s = input("Your guess: ")
        if s.isalpha():
            if len(s) != 1:
                print("Illegal format.")
            elif s.islower():
                s = s.upper()
                if s in ans:
                    for i in range(len(ans)):
                        ch = ans[i]
                        ch1 = p[i]
                        if ch == s:
                            guess += ch
                        else:
                            guess += ch1
                    p = guess
                    if p == ans:
                        print("You are correct!\nYou win!!\nThe word was " + p)
                        break
                    print("You are correct!\nThe word looks like " + p)
                    print("You have " + str(n) + " wrong guesses left.")
                elif s not in ans:
                    n -= 1
                    print("There is no " + s + "'s in the word.")
                    if n == 0:
                        print("You are completely hung :(\nThe word was " + ans)
                        break
                    print("The word looks like " + p)
                    print("You have " + str(n) + " wrong guesses left.")
        elif s.isdigit():
            print("Illegal format.")
        else:
            print("Illegal format.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
