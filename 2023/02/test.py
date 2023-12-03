import unittest
from main import main


class Test202302(unittest.TestCase):
    def test_202302(self):
        result = main("sampleinput.txt")

        self.assertEqual(8, result[0])
        self.assertEqual(2286, result[1])


if __name__ == "__main__":
    unittest.main()
