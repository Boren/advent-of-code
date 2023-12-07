import unittest
from main import main


class Test202306(unittest.TestCase):
    def test_202306(self):
        result = main("sampleinput.txt")

        self.assertEqual(288, result[0])
        # self.assertEqual(46, result[1])


if __name__ == "__main__":
    unittest.main()
