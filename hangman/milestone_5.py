import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(letter)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # attributes
        self.word_list = word_list
        self.num_lives = num_lives

        # attribute defined using other attributes
        self.num_list = 0 # number of unguessed unique letters
        self.list_of_guesses = [] #number of wrong guesses
        self.word = random.choice(word_list) 
        self.num_unique_letters = ""
        self.num_unique_letters = len(self.num_unique_letters.join(set(self.word)))
        self.num_letters = len(self.word)
        self.word_guessed = []
        for self.letter in self.word:
            self.word_guessed.append("_")
        
        print(f"The mystery word has {self.num_letters} characters")
        pass


    # methods
    def check_guess(self, guess):  
        '''
        Checks if the guess input fulfills the criteria of being a single, alphabetic letter.
        If it is, it checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = (guess)
            self.num_unique_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
        pass

    def ask_for_input(self):  
        #while True:
        guess = input(f"Please enter a single letter: ")
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid entry. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You have already tried this letter! ")
        else:              
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(f"List of guessed letters: {self.list_of_guesses}")
        pass

def play_game(word_list):
    '''
        Checks the number of lives left in the game, and the number of unique letters that are not yet guessed.
        If there are at no lives left, the user gets a message saying they lost, along with the correct word.
        If the user has a non-zero number of lives left and still hasn't guessed all unique letters, they are shown
        their current guesses, including the right and wrong answers, told how many lives are left, and prompted to 
        enter another letter, by calling the ask_for_input() method in the Hangman class.
        If the user has a non-zero number of lives left and all unique letters are guessed, the user is shown a 
        message informing that they have won the game

        Parameters:
        ----------
        word_list: list
            A list of strings containing the possible words in the game, the winning word being chosen randomly
        num_lives: int
            An integer value representing the number of lives remaining for the user. Initialised at 5

        '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while num_lives >= 0 and game.num_unique_letters >= 0:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_lives != 0 and game.num_unique_letters > 0:
            print(f"Guessed word: {game.word_guessed}")
            print(f"You have {game.num_lives} lives left")
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_unique_letters == 0:
            print("Congratulations. You won the game!")
            break
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'raspberry']
    play_game(word_list)