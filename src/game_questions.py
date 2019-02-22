""" Game questions class that handles user input (answers) to the questions given from this
    class """

import random


class GameQuestions:
    """ Game questions class"""

    def __init__(self, seed):
        random.seed(seed)
        self.question_number = 0

    def game_questions(self):
        """ The list of game questions to pick at randomly """
        self.question_number = random.randint(0, 4)

        return {
            0: "When you start the game, what recursion level do you start on?",
            1: "What\'s the max level recursion can you achieve with this game?",
            2: "What recursion level are your parents in?",
            3: "What recursion level is the grandmother in?",
            4: "If there wasn't a max level in this tree, what level would the great great"
               "grandparents be located in?",
        }[self.question_number]

    def compare_answers(self, player_input):
        """ Compares the answers with the user input corresponding to the question """
