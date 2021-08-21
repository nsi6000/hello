
from main import *
#hello(user_input)
import unittest

class TestUserInput(unittest.TestCase):

    def test_trivial(self):
        self.assertEqual("ABC","ABC")

    def test_no_input(self):
        self.assertEqual(hello(),"Hello")

    def test_barack(self):
        self.assertEqual("Hello Barack","Hello Barack")
        self.assertEqual(hello("Barack"),"Hello Barack")


if __name__ == '__main__':
    unittest.main()



