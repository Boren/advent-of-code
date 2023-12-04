import unittest
from main import main


class Test202303(unittest.TestCase):
    def test_202303(self):
        result = main("sampleinput.txt")

        self.assertEqual(13, result[0])
        self.assertEqual(30, result[1])


if __name__ == "__main__":
    unittest.main()
