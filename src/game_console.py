""" Game console class that handles user input and front-end display to CLI """
# import time
# import sys


class GameConsole:
    """ Game console class """
    welcome_message = "Welcome to Family Tree: A Real-Life Recursive Example!\n"
    menu = "Play or Quit?\n"
    enter_input = "Please enter an input: "
    error_message = "That is not a correct input!\n"
    game_state = 0

    def __init__(self, game_state):
        self.game_state = game_state

    def start_game(self):
        """ Starts a new game in that a welcome message appears and ask if the user want to play
            or not. """
        print(self.welcome_message)
        print(self.menu)
        user_input = input(self.enter_input)

        play_strings = ["Play", "play", "p"]
        quit_strings = ["Quit", "quit", "q"]

        while 1:
            if user_input in play_strings:
                self.main_game()
                break
            elif user_input in quit_strings:
                self.end_game()
                break
            else:
                print(self.error_message)

    def end_game(self):
        """ Quits the game """
        self.game_state = 0

    def main_game(self):
        """ The actual main game where it will handle user input to create a family tree with n
            amount of levels and takes in user input to traverse that same family tree while
            printing out call stacks and what has been popped and created. """
