from random import randint

MIN = 1
MAX = 100
tries = 0
choice = randint(MIN, MAX)
def check(choice, guess, tries):
    try:
        guess = int(guess)
    except ValueError:
        print("Bad input, try again")
        guess = input("Guess again \n")
        check(choice, guess, tries)
    tries += 1
    if choice == guess:
        print(f"You got it in {tries} tries")
    elif choice > guess:
        print(f"The number is higher than {guess}")
        guess = input("Guess again \n")
        check(choice, guess, tries)
    elif choice < guess:
        print(f"The number is lower than {guess}")
        guess = input("Guess again \n")
        check(choice, guess, tries)



guess = input(("Guess a number between %d and %d \n" % (MIN, MAX)))

check(choice, guess, tries)
