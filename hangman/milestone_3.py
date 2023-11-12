import milestone_2
while True:
    # Custom input validation without explicitly raising ValueError
    guess = input("Please enter a single letter: ")
    if guess.isalpha():
        break
    else:
        raise ValueError("Invalid letter. Please, enter a single alphabetical character.")

if guess in milestone_2.word():
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
