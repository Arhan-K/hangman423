import milestone_2
import random

class Hangman:
    def __init__(self, word_list = milestone_2.word_list, num_lives=5):
        # attributes
        self.word_list = milestone_2.word_list
        self.num_lives = num_lives

        # attribute defined using other attributes
        self.num_list = 0 # number of unguessed unique letters
        self.list_of_guesses = [] #number of wrong guesses
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = []
        for self.letter in self.word:
            self.word_guessed.append("_")


    # methods
    def check_guess(self, guess):  # can add external arguments
        guess = guess.lower()
        if guess in milestone_2.word:
            print(f"Good guess! {guess} is in the word.")
            #indexes = []
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = (guess)
                    #indexes.append(i)
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left") 
        #return self.param1 + ext_input + Cylinder.att

    def ask_for_input(self):  # method to modify attribute
        """while True:
            guess = input("Please enter a single letter: ")
            if not guess.isalpha() and len(guess) == 1:
                raise ValueError("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                raise ValueError("You have already tried this letter! ")
            else:              
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guessed letters: {self.list_of_guesses}") """
        guess = input("Please enter a single letter: ")
        if not guess.isalpha() and len(guess) == 1:
            raise ValueError("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            raise ValueError("You have already tried this letter! ")
        else:              
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(f"List of guessed letters: {self.list_of_guesses}")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        print(game.num_lives)
        if game.num_lives == 0:
            print("You lost!")
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")

play_game(milestone_2.word_list)
#print(milestone_2.word_list)