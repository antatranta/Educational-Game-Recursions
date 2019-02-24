""" Game questions class that handles user input (answers) to the questions given from this
    class """

import random


class GameQuestions:
    """ Game questions class"""

    def __init__(self, seed):
        random.seed(seed)
        self.question_number = 0
        self.questions = []
        self._add_questions_()

    def _add_questions_(self):
        """ Private method that adds questions to the list defined in init """
        question_0 = "When you start the game, what recursion level do you start on?"
        self.questions.append(question_0)

        question_1 = "What\'s the max level recursion can you achieve with this game?"
        self.questions.append(question_1)

        question_2 = "What recursion level are your parents in?"
        self.questions.append(question_2)

        question_3 = "What recursion level is your grandmother in?"
        self.questions.append(question_3)

        question_4 = "If there wasn\'t a max level in this tree, what level would your " \
                     "great great grandparents be located in?"
        self.questions.append(question_4)

    def game_questions(self):
        """ The list of game questions to pick at randomly returns a string of the
            question """
        self.question_number = random.randint(0, len(self.questions) - 1)

        return self.questions.pop(self.question_number)

    def compare_answers(self, player_input):
        """ Compares the answers with the user input corresponding to the question """
