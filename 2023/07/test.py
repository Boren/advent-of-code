import unittest
from main import main


class Test202307(unittest.TestCase):
    def test_202307(self):
        result = main("sampleinput.txt")

        self.assertEqual(6440, result[0])
        self.assertEqual(5905, result[1])


if __name__ == "__main__":
    unittest.main()
