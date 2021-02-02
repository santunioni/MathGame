from models.user_interface import UserInterface
from models.make_user import User


def run_game(*, user_instance: User) -> None:
    if not isinstance(user_instance, User):
        return None
    print(f"Difficulty level set to {user_instance.difficulty_level} for user {user_instance.username}. \
    Starting the game ...")

    for i in range(10):
        answer_to_append = UserInterface.new_question(difficulty_level=user_instance.difficulty_level)
        user_instance.answers_append(answer_to_append=answer_to_append)

    print(user_instance.answers_list)
    print(f"Your score is {user_instance.score}")


def main():

    username: str = input("Tell me an unique username: ")
    full_name: str = input("Tell your full name: ")
    difficulty_level: int = int(input("Tell me the difficulty level you wanna play: "))

    user: User = User(username=username, full_name=full_name)
    user.difficulty_level = difficulty_level

    run_game(user_instance=user)


if __name__ == "__main__":
    main()
