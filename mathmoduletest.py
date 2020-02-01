import unittest
import mathmodule

class MyTestCase(unittest.TestCase):
    mathclass = mathmodule.Math
    def test_2_module3(self):
        self.assertEqual(self.mathclass.module3(2), False)
    def test_3_module3(self):
        self.assertEqual(self.mathclass.module3(3), True)
    def test_5_module3(self):
        self.assertEqual(self.mathclass.module3(5), False)
    def test_6_module3(self):
        self.assertEqual(self.mathclass.module3(6), True)
    def test_10_module3(self):
        self.assertEqual(self.mathclass.module3(10), False)


    def test_2_module5(self):
        self.assertEqual(self.mathclass.module5(2), False)
    def test_3_module5(self):
        self.assertEqual(self.mathclass.module5(3), False)
    def test_5_module5(self):
        self.assertEqual(self.mathclass.module5(5), True)
    def test_6_module5(self):
        self.assertEqual(self.mathclass.module5(6), False)
    def test_10_module5(self):
        self.assertEqual(self.mathclass.module5(10), True)

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

    # def test_myoutput(capsys):
    #     captured = capsys.readouterr()

if __name__ == '__main__':
    unittest.main()
