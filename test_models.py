import unittest
from models.make_user import User
from models.operations import MathOperations
from models.user_interface import UserInterface
from random import randint


class User_Tests(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='my_username', full_name='My Full Name')

    def test_username(self):
        self.assertEqual(self.new_user.username, 'my_username')

    def test_full_name(self):
        self.assertEqual(self.new_user.full_name, 'My Full Name')

    def test_difficulty(self):
        self.assertEqual(self.new_user.difficulty_level, 1)
        self.new_user.difficulty_level = 3
        self.assertEqual(self.new_user.difficulty_level, 3)

    def test_answer_append_score(self):
        self.new_user.answers_append(answer_to_append={'operation': '3+5-2', 'user_answer': 3,
                                                       'correct_answer': 6, 'answered_correctly': False,
                                                       'difficulty_level': 5}
                                     )
        self.assertEqual(self.new_user.answers_list, [{'operation': '3+5-2', 'user_answer': 3,
                                                       'correct_answer': 6, 'answered_correctly': False,
                                                       'difficulty_level': 5}]
                         )
        self.assertEqual(self.new_user.score, -5)

    def tearDown(self):
        del self.new_user


class MathOperations_Tests(unittest.TestCase):

    def test_return_operation(self):
        operation, result = MathOperations.return_operation(difficulty_level=randint(1, 1999))
        self.assertEqual(type(operation), str)
        self.assertEqual(type(result), int)
        self.assertEqual(result, eval(operation))

    def test_prime_check(self):
        self.assertTrue(MathOperations._MathOperations__prime_check(17))
        self.assertTrue(MathOperations._MathOperations__prime_check(19))
        self.assertTrue(MathOperations._MathOperations__prime_check(2))
        self.assertFalse(MathOperations._MathOperations__prime_check(20))
        self.assertFalse(MathOperations._MathOperations__prime_check(1))
        self.assertFalse(MathOperations._MathOperations__prime_check(0))

    def test_dividers_from(self):
        self.assertEqual(MathOperations._MathOperations__dividers_of(20), [2, 4, 5, 10])
        self.assertEqual(MathOperations._MathOperations__dividers_of(17), [])
        self.assertEqual(MathOperations._MathOperations__dividers_of(2), [])


if __name__ == '__main__':
    unittest.main()
