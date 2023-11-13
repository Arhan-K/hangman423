import milestone_2

class Hangman:
    def __init__(self, word_list = milestone_2.word_list, num_lives=5):
        # attributes
        self.word_list = milestone_2.word_list
        self.num_lives = num_lives

        # attribute defined using other attributes
        self.num_list = 0 # number of unguessed unique letters
        self.list_of_guesses = [] #number of wrong guesses
        self.word = word_list.random()
        self.word_guessed = []
        for self.letter in self.word:
            self.word_guessed.append("_")

        # attribute defined without a parameter
        #self.surface_area = None
        #self.volume = None
        
        #self.num_lives = 5

    # methods
    def check_guess(self, guess):  # can add external arguments
        guess = guess.lower()
        if guess in milestone_2.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")    
        #return self.param1 + ext_input + Cylinder.att

    def ask_for_input(self):  # method to modify attribute
        while True:
            guess = input("Please enter a single letter: ")
            if not guess.isalpha() and len(guess) == 1:
                raise ValueError("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                raise ValueError("You have already tried this letter! ")
            else:              
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
hangman = Hangman()
hangman.ask_for_input()