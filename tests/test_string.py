from unittest import TestCase
import unittest


class TestStringMethod(TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".islower())


if __name__ == "__main__":
    unittest.main()
