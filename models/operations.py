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
        basic_operations = rd.choices(MathOperations.__BASIC_OPERATIONS, k=difficulty_level)

        # I defined the maximum number for operations depending on difficulty level according to:
        # https://www.wolframalpha.com/input/?i=plot+10%2Btanh%28%28x-1%29%2F5%29%2889%29%2C+x+%3D+0%2C+10
        number_max = int(10+tanh((difficulty_level-1)/5)*89)

        for basic_operation in basic_operations:

            if basic_operation == "/":
                while MathOperations.__prime_check(number1 := rd.randint(1, number_max)) or number1 == 1:
                    pass
                number2 = rd.choice(MathOperations.__dividers_from(number1))
                operation.append(f"{rd.choice(['+', '-'])} ({number1} {basic_operation} {number2})")
                del number2

            elif basic_operation == "*":
                number1 = rd.randint(1, number_max)
                number2 = rd.randint(1, number_max)
                operation.append(f"{rd.choice(['+', '-'])} ({number1} {basic_operation} {number2})")
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
        dividers = {reduce(lambda x, y: x * y, permutation)
                    for r in range(1, len(prime_factors) + 1) for permutation in permutations(prime_factors, r=r)
                    }
        dividers_except_number = dividers.copy()
        dividers_except_number.remove(number)
        return list(dividers_except_number)
