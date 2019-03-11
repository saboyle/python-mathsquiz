import random
import time
import fire
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Question(object):

    def __init__(self, operators, min_number, max_number, allow_negative_numbers, fix_number=None):
        self.operator = operators[random.randint(0, len(operators) - 1)]

        if self.operator == '/':
            self.numbers = [random.randint(1, max_number) for _i in range(2)]
            self.numbers[0] = self.numbers[0] * self.numbers[1]
        else:
            self.numbers = [random.randint(min_number, max_number) for _i in range(2)]

        if self.operator == '*' and fix_number is not None:
            self.numbers[0] = fix_number

        if not allow_negative_numbers:
            self.numbers = sorted(self.numbers, reverse=True)

        self.text = f"{self.numbers[0]} {self.operator} {self.numbers[1]}"
        self.answer = eval(self.text)

    def mark(self, answer):
        if int(answer) == int(self.answer):
            print("Correct\n")
            return 1
        else:
            print(f"Incorrect - expected {self.answer}\n")
            return 0


class Quiz(object):
    """
    Configurable Maths Quiz
    """

    def __init__(self, name="Student", num_questions=5, min_number=1, max_number=10, operators=['+', '*', '-', '/'],
                 allow_negative_numbers=False, fix_number=None):

        self.name = name
        self.num_questions = num_questions
        self.min_number = min_number
        self.max_number = max_number
        self.operators = operators
        self.allow_negative_numbers = allow_negative_numbers
        self.fix_number = fix_number

        self._correct = 0
        self._incorrect = 0
        self._remaining = self.num_questions
        self._questions = [Question(self.operators, self.min_number, self.max_number, self.allow_negative_numbers,
                                    self.fix_number)
                           for _q in range(self.num_questions)]
        self._time_taken = 0
        self._percent = 0

    def run(self):
        """ Start the Maths practice."""
        clear()
        print("==============")
        print("Maths Practice")
        print("==============")
        start_time = time.time()
        for q in self._questions:
            answer = input(f"{q.text} = ")
            bonus = q.mark(answer)
            if bonus > 0:
                self._correct += bonus
            else:
                self._incorrect += 1
            self._remaining -= 1
        end_time = time.time()
        self._time_taken = end_time - start_time
        print(f"Correct: {self._correct} \nIncorrect: {self._incorrect} \nTime: {self._time_taken:2.2f} seconds\n")
        self._percent = self._correct / len(self._questions)
        self._praise()

    def _praise(self):
        if self._correct == self.num_questions:
            print(f"Well done {self.name} - PERFECT score 100%")
        elif self._correct > self._incorrect:
            print(f"Well done {self.name} Score: {self._percent}")
        else:
            print(f"Well done for practising {self.name} Score: {self._percent}")


if __name__ == '__main__':
    fire.Fire(Quiz)
