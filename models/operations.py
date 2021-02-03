import random as rd
import models.downloaded_algorithms.prime_check as pc
import models.downloaded_algorithms.prime_factors as pf
from itertools import permutations
from functools import reduce
from math import tanh


class MathOperations:

    __BASIC_OPERATIONS = ("+", "-", "*", "/")
    __float_allowed = False

    @staticmethod
    def return_operation(*, difficulty_level: int) -> tuple[str, int]:
        """Returns a random math operation and it's result, given the difficulty_level.
        The returned operation is in the format: {operation: string, result: eval(operation)}"""
        operation = MathOperations.__operation(difficulty_level=difficulty_level)
        result = int(eval(operation))
        return operation, result

    @staticmethod
    def __operation(*, difficulty_level):
        operation = []

        # We will randomly choose what operations from __BASIC_OPERATIONS the function will return to the player.
        # The difficulty_level sets how many operations the player will have to compute in a single math expression.
        # The next lines sets basic_operations as a list with length 'difficulty_level' containing the four basic
        # math operations. The math operations may repeat, of course.
        basic_operations = rd.choices(MathOperations.__BASIC_OPERATIONS, k=difficulty_level)

        # I defined the maximum number the player will have to compute depending on difficulty level according to:
        # https://www.wolframalpha.com/input/?i=plot+10%2Btanh%28%28x-1%29%2F5%29%2889%29%2C+x+%3D+0%2C+10
        number_max = int(10+tanh((difficulty_level-1)/5)*89)

        # The for loop set numbers in between the operations that were chosen in basic_operations
        for basic_operation in basic_operations:

            if basic_operation == "/":
                while MathOperations.__prime_check(number1 := rd.randint(1, number_max)) or number1 == 1:
                    pass
                number2 = rd.choice(MathOperations.__dividers_from(number1))
                if difficulty_level > 1:
                    operation.append(f"{rd.choice(['+', '-'])}")
                operation.append(f"({number1} {basic_operation} {number2})")
                del number2

            elif basic_operation == "*":
                number1 = rd.randint(1, number_max)
                number2 = rd.randint(1, number_max)
                if difficulty_level > 1:
                    operation.append(f"{rd.choice(['+', '-'])}")
                operation.append(f"({number1} {basic_operation} {number2})")
                del number2

            elif basic_operation == "+":
                number1 = rd.randint(1, number_max)
                operation.append("+")
                operation.append(f"{number1}")

            elif basic_operation == "-":
                number1 = rd.randint(1, number_max)
                operation.append("-")
                operation.append(f"{number1}")

            del number1

        if operation[0] == '+' or operation[0] == '-':
            operation = [str(rd.randint(1, number_max)), *operation]

        operation = ' '.join(operation)
        return operation

    @staticmethod
    def __prime_check(number: int) -> bool:
        return pc.prime_check(number)

    @staticmethod
    def __dividers_from(number: int) -> list[int]:
        prime_factors = pf.prime_factors(number)
        dividers = {
                    # The next line returns all numbers multiplied from a given permutation
                    reduce(lambda x, y: x*y, permutation)
                    # The next line spams all possible lengths of permutation lists from the prime_factor list
                    for permutation_length in range(1, len(prime_factors)+1)
                    # The next line runs over the many permutations from prime_factors with length permutation_length
                    for permutation in permutations(prime_factors, r=permutation_length)
                    }
        dividers_except_number = dividers.copy()
        dividers_except_number.remove(number)
        return list(dividers_except_number)
