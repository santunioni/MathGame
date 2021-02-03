from models.operations import MathOperations


class UserInterface:

    @staticmethod
    def new_question(*, difficulty_level: int) -> dict:

        # Requesting random math operation
        operation, result = UserInterface.__operation_request(difficulty_level=difficulty_level)

        # Operation printing and user input
        user_answer = UserInterface.__answer_request(operation=operation)

        return {'operation': operation,
                'result': result,
                'user_answer': user_answer,
                'answered_correctly': result == user_answer}

    @staticmethod
    def __operation_request(*, difficulty_level: int) -> tuple[str, int]:
        """Request the Math Operation from the class MathOperation."""
        operation, result = MathOperations.return_operation(difficulty_level=difficulty_level)
        return operation, result

    @staticmethod
    def __answer_request(*, operation: str) -> int:
        """Request the user to input the answer for the question."""
        UserInterface.__operation_present(operation=operation)

        keep_asking = True
        while keep_asking:
            try:
                user_answer: int = int(input())
                keep_asking = False
            except ValueError:
                print("Your answer should be an integer number!")
                UserInterface.__operation_present(operation=operation)
        del keep_asking

        return user_answer

    @staticmethod
    def __operation_present(*, operation: str) -> None:
        print(operation + " = ", end="")
