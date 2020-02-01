import unittest
import mathmodule

class MyTestCase(unittest.TestCase):
    mathclass = mathmodule.FizzBuzzChecker
    def test_2_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(2), False)
    def test_3_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(3), True)
    def test_5_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(5), False)
    def test_6_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(6), True)
    def test_10_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(10), False)
    def test_13_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(13), True)
    def test_0_isFizz(self):
        self.assertEqual(self.mathclass.isFizz(0), False)
    def test_2_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(2), False)
    def test_3_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(3), False)
    def test_5_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(5), True)
    def test_6_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(6), False)
    def test_10_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(10), True)
    def test_52_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(52), True)
    def test_0_isBuzz(self):
        self.assertEqual(self.mathclass.isBuzz(0), False)
    def test_2_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(2), "2")
    def test_3_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(3), "Fizz")
    def test_5_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(5), "Buzz")
    def test_6_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(6), "Fizz")
    def test_10_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(10), "Buzz")
    def test_15_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(15), "FizzBuzz")
    def test_35_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(35), "FizzBuzz")
    def test_53_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(53), "FizzBuzz")
    def test_0_checkFizzBuzz(self):
        self.assertEqual(self.mathclass.checkFizzBuzz(0), "0")
    # def test_myoutput(capsys):
    #     captured = capsys.readouterr()

if __name__ == '__main__':
    unittest.main()
