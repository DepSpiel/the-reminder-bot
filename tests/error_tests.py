#***
#@author BW Babcock
#@This file constitutes a few tests for the filter.py file.
#***
import unittest #import Python's unittest package.
import sys
sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot') #'/home/ubuntu/thereminderbot/thereminderbot'
from tweet import Tweet #import the class meant to create the tweets for testing.
from error import FilterError #import my filter file (the file being tested)

class ErrorTest(unittest.TestCase):
	#Each function indicates a test case for the filter.py file.

	def test_filter1(self): #This test should pass, and is meant to establish a baseline.
		tweet_1 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "This should pass", "n/a")
		self.assertEqual(tweet_1.msg, "This should pass")

	def test_filter2(self): #This test should raise a FilterError.
		tweet_2 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "Fuck--this--shit", "n/a")
		self.assertRaises(FilterError)

	def test_filter3(self): #This test should raise a FilterError.
		tweet_3 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "Fuckthisshit", "n/a")
		self.assertRaises(FilterError)

	def test_filter4(self): #This test should raise a FilterError.
		tweet_4 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "Fuck     this     shit", "n/a")
		self.assertRaises(FilterError)

	def test_filter5(self): #This test should raise a FilterError.
		tweet_5 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "Fuck_this_shit", "n/a")
		self.assertRaises(FilterError)

	def test_filter6(self): #This test should raise a FilterError.
		tweet_6 = Tweet("@trapkingwillie", 1, 12, "PM", "Eastern Time (US & Canada)", 10, 15, "asd_Fuck-this&shit", "n/a")
		self.assertRaises(FilterError)

if __name__ == '__main__':
	unittest.main()
