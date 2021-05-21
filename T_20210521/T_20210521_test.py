import unittest
from T_20210521 import Calculator


class TDD(unittest.TestCase):

    def test_add(self):
        calc = Calculator(False)
        expected = 5
        got = calc.add(2,3)
        self.assertEqual(expected, got)

    def test_sub(self):
        calc = Calculator(False)
        expected = -1
        got = calc.sub(2,3)
        self.assertEqual(expected, got)

    def test_mul(self):
        calc = Calculator(False)
        expected = 6
        got = calc.mul(2,3)
        self.assertEqual(expected, got)

    def test_div_1(self):
        calc = Calculator(False)
        expected = 2
        got = calc.div_1(10,5)
        self.assertEqual(expected, got)

    def test_div_2(self):
        calc = Calculator(False)
        with self.assertRaises(AssertionError): calc.div_2(10,0)

    def test_div_3(self):
        calc = Calculator(False)
        got = calc.div_3(10,0)
        self.assertFalse(got[1])
        
    def test_calculate_1(self): 
        calc = Calculator(False)
        expected = 5
        got = calc.calculate(2, 3, "+")
        self.assertEqual(expected, got)     
        
    def test_calculate_2(self): 
        calc = Calculator(False)
        expected = 3.0
        got = calc.calculate(9, 3, "/")
        self.assertEqual(expected, got[0])        

if __name__ == "__main__":
    unittest.main()
