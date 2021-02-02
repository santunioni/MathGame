from models.operations import MathOperations


class UserInterface:

    @staticmethod
    def new_question(*, difficulty_level: int) -> dict:

        # Requesting random math operation
        operation, result = UserInterface.__operation_request(difficulty_level=difficulty_level)

        # Operation printing and user input
        UserInterface.__operation_present(operation=operation)
        user_answer = UserInterface.__answer_request()

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
    def __operation_present(*, operation: str) -> None:
        print(operation + " = ", end="")

    @staticmethod
    def __answer_request() -> int:
        """Request the user to input the answer for the question."""
        return int(input())

