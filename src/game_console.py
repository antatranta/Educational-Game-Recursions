""" Game console class that handles user input and front-end display to command line interface """

import time
import sys
from family_tree import FamilyTree


class GameConsole:
    """ Game console class """

    def __init__(self):
        self.enter_input = "Please enter an input: "
        self.error_message = "That is not a correct input!"
        self.game_state = 0
        self.player_family_tree = None
        self.recursion_level = 0

    def start_game(self):
        """ Starts a new game in that a welcome message appears and ask if the user want to play
            or not. """
        welcome_message = "Welcome to Family Tree: A Real-Life Recursive Example!\n"
        menu = "Play or Quit?"

        print(welcome_message)
        print(menu)

        play_strings = ["Play", "play", "p", "P"]
        quit_strings = ["Quit", "quit", "q", "Q"]

        while 1:
            user_input = input(self.enter_input)

            if user_input in play_strings:
                self.main_game()
                break
            elif user_input in quit_strings:
                self.end_game()
                break
            else:
                print(self.error_message)

    @staticmethod
    def end_game():
        """ Quits the game """
        print("Quitting the game in 5 seconds\n")
        time.sleep(5)
        sys.exit("Ended Game")

    def print_current_node(self):
        """ Prints out where you are currently in the family tree and the root in addition to
            the recursion level """
        print(self.player_family_tree)

        current_node = "This is where you are currently at in the family tree: "
        print(current_node, self.player_family_tree.head)

        recursion_message = "This is where you are on the recursion level: "
        print(recursion_message, self.recursion_level)

    def main_game(self):
        """ The actual main game where it will handle user input to create a family tree that
            takes in user input to traverse that same family tree while printing out call
            stacks and what has been popped and created. """
        get_player_name = "What is your name?\n"
        print(get_player_name)
        player_name = input(self.enter_input)
        self.player_family_tree = FamilyTree(player_name)

        game_message = "Here is your family tree starting with you\n"
        print(game_message)

        self.print_current_node()

        traverse_message = "Where do you want to go? (M)other or (F)ather. You can also " \
                           "type (l)eft or (r)ight (left for mother and right for father)."
        print(traverse_message)

        traverse_mother = ["Mother", "mother", "M", "m", "Left", "left", "L", "l"]
        traverse_father = ["Father", "father", "F", "f", "Right", "right", "R", "r"]

        user_traverse_input = input(self.enter_input)

        # TODO: Finish up main_game for command line interface
        if user_traverse_input in traverse_mother:
            self.player_family_tree.go_to_mother()
        elif user_traverse_input in traverse_father:
            self.player_family_tree.go_to_father()
        else:
            print(self.error_message)
