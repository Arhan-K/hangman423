import milestone_2

def check_guess(guess):
    guess = guess.lower()
    if guess in milestone_2.word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        if guess.isalpha():
            break
        else:
            raise ValueError("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
