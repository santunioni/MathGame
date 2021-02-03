class User:

    def __init__(self, *, username: str, full_name: str, difficulty_level: int = 1):
        if User.__user_already_exist(username):
            raise UserWarning
        self.__username = username.lower()
        self.__full_name = full_name.title()
        self.__difficulty_level = difficulty_level
        self.__answers_list: list[dict] = []

    @property
    def username(self):
        return self.__username

    @property
    def full_name(self):
        return self.__full_name

    @property
    def answers_list(self):
        return self.__answers_list

    @property
    def score(self):
        individual_score = [answer.get('difficulty_level')**2 if answer.get('answered_correctly')
                            else -answer.get('difficulty_level')
                            for answer in self.__answers_list]
        return sum(individual_score)

    @property
    def difficulty_level(self):
        return self.__difficulty_level

    @difficulty_level.setter
    def difficulty_level(self, difficulty_level):
        if type(difficulty_level) == int and difficulty_level > 0:
            self.__difficulty_level = difficulty_level

    @staticmethod
    def __user_already_exist(username: str):
        return False

    @staticmethod
    def ask_difficulty_level() -> int:
        keep_asking = True
        while keep_asking:
            try:
                difficulty_level: int = int(input("Tell me the difficulty level you wanna play: "))
                keep_asking = False
                if difficulty_level <= 0:
                    print("The difficulty level is a positive integer!")
                    keep_asking = True
            except ValueError:
                print("The difficulty level is a positive integer!")
        return difficulty_level

    def answers_append(self, *, answer_to_append: dict) -> None:
        self.__answers_list.append(
            answer_to_append
        )

    def answers_export(self):
        pass
