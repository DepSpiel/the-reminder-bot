"""
@author <Lacey Perry>
<Some basic test cases for Time.py>
"""

import unittest
from thereminderbot.error import CreateTweetError
from thereminderbot.time import convert_time_zone, time_check
from thereminderbot.tweet import Tweet

class TimeTest(unittest.TestCase):
	
	#test cases for convert_time_zone
	def test_ctz1(self):
		tz=Tweet("@bob", 4, 32, "AM", "Pacific Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,7)
		self.assertEqual(tz.period,"AM")

	def test_ctz2(self):
		tz=Tweet("@bob", 11, 32, "AM", "Pacific Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,2)
		self.assertEqual(tz.period,"PM")

	def test_ctz3(self):
		tz=Tweet("@bob", 12, 32, "AM", "Pacific Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,3)
		self.assertEqual(tz.period,"AM")
	
	def test_ctz4(self):
		tz=Tweet("@bob", 0, 32, "AM", "Eastern Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,0)
		self.assertEqual(tz.period,"AM")

	def test_ctz5(self):
		tz=Tweet("@bob", 0, 32, "AM", "Central Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,1)
		self.assertEqual(tz.period,"AM")
		
	def test_ctz6(self):
		tz=Tweet("@bob", 12, 32, "PM", "Central Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,1)
		self.assertEqual(tz.period,"PM")
	
	def test_ctz7(self):
		tz=Tweet("@bob", 12, 32, "AM", "Central Time (US & Canada)", 10, 15, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,1)
		self.assertEqual(tz.period,"AM")
		
	def test_ctz8(self):
		tz=Tweet("@bob", 12, 32, "AM", "Central Time (US & Canada)", 11, 21, "Hi", "none")
		inEST=convert_time_zone(tz)
		self.assertEqual(tz.hour,1)
		self.assertEqual(tz.period,"AM")
	
	#exceptionhandling for convert_time_zone
	def test_ctze1(self):
		tz=Tweet("@bob", 13, 32, "AM", "Central Time (US & Canada)", 10, 21, "Hi", "none")
		self.assertRaises(CreateTweetError, lambda: time_check(tz))
		
	def test_ctze2(self):
		tz=Tweet("@bob", 13, 32, "PM", "Central Time (US & Canada)", 10, 21, "Hi", "none")
		self.assertRaises(ValueError, lambda: time_check(tz))
	
	#test cases for time_check
	def test_tcheck(self):
		tz=Tweet("@bob", 12, 32, "AM", "Central Time (US & Canada)", 10, 21, "Hi", "none")
		self.assertRaises(CreateTweetError, lambda: time_check(tz))
	
	#test cases for time_check
	def test_tcheck1(self):
		tz=Tweet("@bob", 13, 32, "AM", "Central Time (US & Canada)", 10, 21, "Hi", "none")
		self.assertRaises(CreateTweetError, lambda: time_check(tz))
		
	def test_tcheck2(self):
		tz=Tweet("@bob", 13, 32, "PM", "Central Time (US & Canada)", 10, 21, "Hi", "none")
		self.assertRaises(ValueError, lambda: time_check(tz))
		
	#this one will pass and return none
	def test_tcheck3(self):
		tz=Tweet("@bob", 12, 32, "AM", "Central Time (US & Canada)", 12, 21, "Hi", "none")
		self.assertEqual(None, time_check(tz))
		

if __name__ == '__main__':
	unittest.main()
