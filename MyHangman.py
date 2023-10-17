# Hangman 

print("\nWelcome to Hangman!")
print("-------------------")

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

import random 
word = random.choice(WORDS).decode()
word = word.upper()

print(f"\nThe word is: {len(word) * '_'}")

def hangman(wrong):
    if wrong == 0:
        hangman_str = '\n+----\n    |\n    |\n    |\n   ---\n'
    elif wrong == 1:
        hangman_str = '\n+----\nO   |\n    |\n    |\n   ---\n'
    elif wrong == 2:
        hangman_str = '\n+----\nO   |\n|   |\n    |\n   ---\n'
    elif wrong == 3:
        hangman_str = '\n +----\n O  |\n/|  |\n    |\n   ---\n'
    elif wrong == 4:
        hangman_str = '\n +----\n O  |\n/|\ |\n    |\n   ---\n'
    elif wrong == 5:
        hangman_str = '\n +----\n O  |\n/|\ |\n/   |\n   ---\n'
    elif wrong == 6:
        hangman_str = '\n +----\n O  |\n/|\ |\n/ \ |\n   ---\n'
    return hangman_str

def print_hangman(amt_wrong):
    if amt_wrong == 1:
        print(hangman(1))
    if amt_wrong == 2:
        print(hangman(2))
    if amt_wrong == 3:
        print(hangman(3))
    if amt_wrong == 4:
        print(hangman(4))
    if amt_wrong == 5:
        print(hangman(5))
    if amt_wrong == 6:
        print(hangman(6))

def gameline(guess):
    for char in word:
        if char in guess:
            print(char, end='')
        else:
            print('_', end='')
    print()

amt_wrong = 0
correct_guess = []
total_guess = []

while (amt_wrong != 6) and (len(correct_guess) != len(set(word))):
    user_guess = input("\nEnter a letter: ").upper()
    if (not user_guess.isalpha()) or (len(user_guess) != 1):
        print(hangman(amt_wrong))
        print("Invalid guess, try again.")
        continue
    if user_guess in word:
        if user_guess not in correct_guess:
            correct_guess.append(user_guess) 
            total_guess.append(user_guess)
        else:
            print(hangman(amt_wrong))
            gameline(correct_guess)
            print("Already guessed, try again.")
            continue
        print(hangman(amt_wrong))
        gameline(correct_guess)
        print("Total guesses: ", end='')
        print(total_guess)
    else:
        amt_wrong += 1
        print(hangman(amt_wrong))
        gameline(correct_guess)
        if user_guess in total_guess:
            print(hangman(amt_wrong))
            print("Already guessed, try again.")
        else:
            print("Wrong, Try again")
            total_guess.append(user_guess)  
        print("Total guesses: ", end='')
        print(total_guess)
        
if amt_wrong == 6:
    print(f"\nSorry, you lost. The word was: {word}")
else:
    print("\nCongratulations, you won!")
    
