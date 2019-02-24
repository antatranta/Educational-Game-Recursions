""" Game questions class that handles user input (answers) to the questions given from this
    class """

import random


class GameQuestions:
    """ Game questions class"""

    def __init__(self, seed):
        random.seed(seed)
        self.question_number = 0
        self.questions = []
        self.answers = []
        self._add_questions_and_answers_()

    def _add_questions_and_answers_(self):
        """ Private method that adds questions to the list defined in init """
        question_0 = "\nWhen you start the game, what recursion level do you start on?"
        answer_0 = 0
        self.questions.append(question_0)
        self.answers.append(answer_0)

        question_1 = "\nWhat\'s the max level recursion can you achieve with this game?"
        answer_1 = 2
        self.questions.append(question_1)
        self.answers.append(answer_1)

        question_2 = "\nWhat recursion level are your parents in?"
        answer_2 = 1
        self.questions.append(question_2)
        self.answers.append(answer_2)

        question_3 = "\nWhat recursion level is your grandmother in?"
        answer_3 = 2
        self.questions.append(question_3)
        self.answers.append(answer_3)

        question_4 = "\nIf there wasn\'t a max level in this tree, what level would your " \
                     "great great grandparents be located in?"
        answer_4 = 5
        self.questions.append(question_4)
        self.answers.append(answer_4)

    def game_questions(self):
        """ The list of game questions to pick at randomly returns a string of the
            question """
        self.question_number = random.randint(0, len(self.questions) - 1)

        return self.questions[self.question_number]

    def compare_answers(self):
        """ Compares the answers with the user input corresponding to the question """
        if len(self.questions) == 0:  # pylint: disable=len-as-condition
            print("\nGAME DONE\n")
        else:
            print(self.game_questions())
            while True:
                try:
                    prompt = "\nEnter your answer: "
                    answer = int(input(prompt))
                except ValueError:
                    print("\nIncorrect Value! Needs to be integer value.\n")
                    continue
                else:
                    break
            if int(answer) == self.answers[self.question_number]:
                print("\nCorrect!")
                del self.questions[self.question_number]
                del self.answers[self.question_number]
                self.compare_answers()
            else:
                print("\nIncorrect! Try Again: \n")
                self.compare_answers()
