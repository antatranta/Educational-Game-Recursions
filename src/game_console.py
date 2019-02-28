""" Game console class that handles user input and front-end display to command line interface """
import threading
import time
import sys
import os

from game_graphical import GameGraphical
from family_tree import FamilyTree
from family_tree_node import FamilyTreeNode
from game_questions import GameQuestions


class GameConsole:
    """ Game console class """

    animation_speed = 1 # number of seconds between animation frames

    def __init__(self, tree=None):
        self.enter_input = "Please enter an input: "
        self.error_message = "That is not a correct input!"
        self.player_family_tree = tree
        self.quit_strings = ["quit", "q"]
        self.gui = None

    def start_game(self):
        """ Starts a new game in that a welcome message appears and ask if the user want to play
            or not. """
        welcome_message = "Welcome to Family Tree: A Real-Life Recursive Example!\n"
        menu = "Play or Quit?"

        print(welcome_message)
        print(menu)

        play_strings = ["play", "p"]

        while 1:
            user_input = input(self.enter_input).lower()

            if user_input in play_strings:
                if self.player_family_tree is None:
                    get_player_name = "What is your name?"
                    print(get_player_name)
                    player_name = input(self.enter_input)
                    tree = self._initialize_tree(player_name)
                    self.player_family_tree = tree

                threading.Thread(target=self.main_game, daemon=True).start()
                self.gui = GameGraphical(tree=self.player_family_tree)
                self.gui.start_game()
                break

            elif user_input in self.quit_strings:
                self._end_game_()
                break
            else:
                print(self.error_message)

    @staticmethod
    def _end_game_():
        """ Quits the game """
        sys.exit("Ended Game")

    def _print_current_family_tree_(self):
        """ Prints out where you are currently in the family tree and the root in addition to
            the recursion level """
        family_tree_message = "Here is your family tree:\n"
        print(family_tree_message)
        print(self.player_family_tree.tree_string)

        current_node = "This is where you are currently at in the family tree: \n"
        print(current_node)
        self._print_whole_family_tree_(0)

        recursion_message = "\nThis is where you are on the recursion level: "
        print(recursion_message, self.player_family_tree.depth, "\n", sep='')

    def _print_whole_family_tree_(self, iteration, indent=""):
        """ Prints out the user's family tree with tabs so it shows how deep the recursion
            is """
        print_family_tree = self.player_family_tree.call_stack

        while 1:
            print(indent, print_family_tree[iteration], sep='')

            if iteration < self.player_family_tree.depth:
                self._print_whole_family_tree_(iteration+1, indent+"    ")

            break

    @classmethod
    def _initialize_tree(cls, player_name):
        father = FamilyTreeNode("Father", FamilyTreeNode("Dad's Dad"), FamilyTreeNode("Dad's Mom"))
        mother = FamilyTreeNode("Mother", FamilyTreeNode("Mom's Dad"), FamilyTreeNode("Mom's Mom"))
        player = FamilyTreeNode(player_name, father, mother)
        return FamilyTree(player)

    @classmethod
    def _clear(cls):
        """Clear the console of all text."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def _game_question_():
        question = GameQuestions(time.time())
        question.compare_answers()

    def _play_traversal(self, traverser):
        """Play traversal animation in console."""
        self.gui.start_traversal(traverser)
        output = []

        for state in traverser:
            self._clear()
            print(self.player_family_tree.tree_string)
            print("Call Stack:", [str(e) for e in self.player_family_tree.call_stack])

            if state is traverser.states.ACTION:
                print(f"print({self.player_family_tree.head})")
                output.append(f"'{self.player_family_tree.head}'")

            print("Output:", " ".join(output))

            time.sleep(self.animation_speed)
        self.gui.end_traversal()

    def main_game(self):
        """ The actual main game where it will handle user input to create a family tree that
            takes in user input to traverse that same family tree while printing out call
            stacks and what has been popped and created. """
        while 1:
            self._print_current_family_tree_()
            self.display_commands()
            self.await_command()

    def display_commands(self):
        """Display available commands in the console."""
        traverse_message = ("Where do you want to go?\n"
                            "    (M)other (F)ather")

        if self.player_family_tree.depth > 0:
            traverse_message += "(C)hild."

        traverse_message += ("\nYou can also:\n"
                             "    play (in)order traversal\n"
                             "    play (pre)order traversal\n"
                             "    play (post)order traversal\n"
                             "    play (g)ame\n"
                             "    (Q)uit")

        print(traverse_message)

    def await_command(self):
        """Wait for and execute user command."""
        traverse_child = ["child", "c", "back", "b"]
        traverse_father = ["father", "f", "left", "l"]
        traverse_mother = ["mother", "m", "right", "r"]
        play_inorder = ["in", "inorder"]
        play_preorder = ["pre", "preorder"]
        play_postorder = ["post", "postorder"]
        play_game = ["game", "g"]

        while 1:
            user_traverse_input = input(self.enter_input).lower()

            if self.player_family_tree.depth > 0 and user_traverse_input in traverse_child:
                self.player_family_tree.go_to_child()
                break

            elif user_traverse_input in traverse_mother:
                self.player_family_tree.go_to_mother()
                break

            elif user_traverse_input in traverse_father:
                self.player_family_tree.go_to_father()
                break

            elif user_traverse_input in play_inorder:
                self._play_traversal(self.player_family_tree.inorder())
                break

            elif user_traverse_input in play_preorder:
                self._play_traversal(self.player_family_tree.preorder())
                break

            elif user_traverse_input in play_postorder:
                self._play_traversal(self.player_family_tree.postorder())
                break

            elif user_traverse_input in self.quit_strings:
                self._end_game_()
                break

            elif user_traverse_input in play_game:
                self._game_question_()
                break

            else:
                print(self.error_message)
