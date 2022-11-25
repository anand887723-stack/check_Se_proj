#!/usr/bin/python3
import unittest

from test_p1 import getSum

class test(unittest.TestCase):
  def test_1(self):
    data = []
    for  i in range(10):
      data.append(i)
    ans = getSum(data)
    self.assertEqual(ans, 45)
    
	def test_2(self):
    data = [1,2,3,4]
    
    ans = getSum(data)
    self.assertEqual(ans, 10)
	    
	def test_3(self):
    data = [1,2,3,4,5]
    
    ans = getSum(data)
    self.assertEqual(ans, 15)
	    
	def test_4(self):
    data = [1,2,3,4]
    
    ans = getSum(data)
    self.assertEqual(ans, 102)
	    
	def test_5(self):
    data = [1,2,3,4]
    
    ans = getSum(data)
    self.assertEqual(ans, 100)
    
if __name__== '__main__':
  unittest.main()
