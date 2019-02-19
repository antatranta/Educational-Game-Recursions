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
        self.quit_strings = ["Quit", "quit", "q", "Q"]

    def start_game(self):
        """ Starts a new game in that a welcome message appears and ask if the user want to play
            or not. """
        welcome_message = "Welcome to Family Tree: A Real-Life Recursive Example!\n"
        menu = "Play or Quit?"

        print(welcome_message)
        print(menu)

        play_strings = ["Play", "play", "p", "P"]

        while 1:
            user_input = input(self.enter_input)

            if user_input in play_strings:
                self.main_game()
                break
            elif user_input in self.quit_strings:
                self._end_game_()
                break
            else:
                print(self.error_message)

    @staticmethod
    def _end_game_():
        """ Quits the game """
        print("Quitting the game in 3 seconds\n")
        time.sleep(3)
        sys.exit("Ended Game")

    def _print_current_family_tree_(self):
        """ Prints out where you are currently in the family tree and the root in addition to
            the recursion level """
        family_tree_message = "Here is your family tree:\n"
        print(family_tree_message)
        self._print_whole_family_tree_(0)

        print("\n", self.player_family_tree, sep='')

        current_node = "This is where you are currently at in the family tree: "
        print(current_node, self.player_family_tree.head)

        recursion_message = "This is where you are on the recursion level: "
        print(recursion_message, self.recursion_level, "\n", sep='')

    def _print_whole_family_tree_(self, iteration, indent=""):
        """ Prints out the user's family tree with tabs so it shows how deep the recursion
            is """
        print_family_tree = self.player_family_tree.whole_family_tree

        while 1:
            print(indent, print_family_tree[iteration], sep='')

            if iteration < self.recursion_level:
                self._print_whole_family_tree_(iteration+1, indent+"    ")

            break

    def main_game(self):
        """ The actual main game where it will handle user input to create a family tree that
            takes in user input to traverse that same family tree while printing out call
            stacks and what has been popped and created. """
        get_player_name = "What is your name?"
        print(get_player_name)
        player_name = input(self.enter_input)
        self.player_family_tree = FamilyTree(player_name)

        while 1:
            self._print_current_family_tree_()

            if self.recursion_level == 0:
                traverse_message = "Where do you want to go? (M)other or (F)ather. You can also " \
                                   "type (l)eft or (r)ight (left for mother and right for " \
                                   "father). You can also (q)uit."
            else:
                traverse_message = "Where do you want to go? (M)other, (F)ather, or (C)hild. " \
                                   "You can also type (l)eft, (r)ight, or (b)ack (left for " \
                                   "mother, right for father, and back for child). You can also " \
                                   "(q)uit."

            print(traverse_message)

            traverse_child = ["Child", "child", "C", "c", "Back", "back", "B", "b"]
            traverse_mother = ["Mother", "mother", "M", "m", "Left", "left", "L", "l"]
            traverse_father = ["Father", "father", "F", "f", "Right", "right", "R", "r"]

            while 1:
                user_traverse_input = input(self.enter_input)

                if self.recursion_level > 0:
                    if user_traverse_input in traverse_child:
                        self.player_family_tree.go_to_child()
                        self.recursion_level -= 1
                        break
                if user_traverse_input in traverse_mother:
                    self.player_family_tree.go_to_mother()
                    self.recursion_level += 1
                    break
                elif user_traverse_input in traverse_father:
                    self.player_family_tree.go_to_father()
                    self.recursion_level += 1
                    break
                elif user_traverse_input in self.quit_strings:
                    self._end_game_()
                    break
                else:
                    print(self.error_message)
