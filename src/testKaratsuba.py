import unittest
import karatsuba
import random

#Invalid characters test
class invalidtest(unittest.TestCase):
    def test1(self):
        self.assertEqual(karatsuba.multp('a','b'),False)

#Negative integers tests
class negativetest(unittest.TestCase):
    def test6(self):
        a,b=random.randint(-99,-10),random.randint(10,99)
        self.assertEqual(karatsuba.multp(a,b),a*b)
    def test7(self):
        a,b=random.randint(10,99),random.randint(-99,-10)
        self.assertEqual(karatsuba.multp(a,b),a*b)
    def test8(self):
        a,b=random.randint(-99,-10),random.randint(-99,-10)
        self.assertEqual(karatsuba.multp(a,b),a*b)
        
#Big integer test
class bigtest(unittest.TestCase):
    def test11(self):
        a,b=random.randint(10000000000000000000000000000,1000000000000000000000000000000),random.randint(10000000000000000000000000000,1000000000000000000000000000000)
        self.assertEqual(karatsuba.multp(a,b),a*b)

#Different size numbers tests
class diffsiztest(unittest.TestCase):
    def test16(self):
        a,b=random.randint(100000,999999),random.randint(1000,9999)
        self.assertEqual(karatsuba.multp(a,b),a*b)
    def test17(self):
        a,b=random.randint(1000,9999),random.randint(100000,999999)
        self.assertEqual(karatsuba.multp(a,b),a*b)
    def test18(self):
        a,b=random.randint(-99,-10),random.randint(-99,-10)
        self.assertEqual(karatsuba.multp(a,b),a*b)

#Odd sized numbers tests
class oddsiztest(unittest.TestCase):
    def test21(self):
        a,b=random.randint(100,999),random.randint(100,999)
        self.assertEqual(karatsuba.multp(a,b),a*b)
    def test22(self):
        a,b=random.randint(1000000,9999999),random.randint(1000000,9999999)
        self.assertEqual(karatsuba.multp(a,b),a*b)

if __name__ == '__main__':
    unittest.main()