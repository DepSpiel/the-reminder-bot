# ***
# @author BW Babcock
# @description This file constitutes a few more (obscure time zone) tests for the verifytime.py file.
# ***

import unittest  # import Python's unittest package.
import sys

sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')
from tweet import Tweet  # import the class meant to create the tweets for testing.
from tweet import CreateTweetError  # import my filter file (the file being tested)
from verifytime import convert_time_zone
from verifytime import time_check

#test cases need to  have different names so I incremented your test case numbers

class TimeTest3(unittest.TestCase):
    # Each function indicates a test case for the filter.py file. This file and the tests within it are based on time_tests_2, with a few additions (testing 'null', etc.)

    
    #Note: Times within the assertEqual line are in Eastern Time.
    def test_time1(self):
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "International Date Line West", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 7)

     def test_time2(self): 
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Midway Island", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 7)

    def test_time3(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "American Samoa", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 7)

    def test_time4(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Hawaii", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 6)

    def test_time5(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Alaska", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 4)

    def test_time6(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Tijuana", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 3)

    def test_time7(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Arizona", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 3)

    def test_time8(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Mountain Time (US & Canada)", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 2)

    def test_time9(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Mazatlan", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 2)

    def test_time10(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Mexico City", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 1)

    def test_time11(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Caracas", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 12)

    def test_time12(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "La Paz", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 12)

    def test_time13(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Georgetown", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 12)

    def test_time14(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Santiago", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 11)
	
	#fixed this test case to reflect the extra half hour difference in timezones
    def test_time15(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Newfoundland", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 10)
		self.assertEqual(tweet_1.minute, 30)

    def test_time16(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Greenland", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 10)

    def test_time17(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Cape Verde Is.", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 9)

    def test_time18(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Azores", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 8)

    def test_time19(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "London", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 7)

    def test_time20(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Belgrade", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 6)

    def test_time21(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Bucharest", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 5)

    def test_time22(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Tehran", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 4)

    def test_time23(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Abu Dhabi", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 4)

    def test_time24(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Kabul", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 3)

    def test_time25(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Islamabad", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 3)

	#fixed this test to account for extra 45 minutes offset
    def test_time26(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Kathmandu", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 2)
		self.assertEqual(tweet_1.minute,15)

    def test_time27(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Astana", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 2)

    def test_time28(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Rangoon", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 1)

    def test_time29(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Bangkok", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 1)

    def test_time30(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Beijing", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 12)

    def test_time31(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Seoul", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 11)

    def test_time32(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Brisbane", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 10)

	#added check to make sure this happens on correct day
    def test_time33(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Adelaide", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 9)
		self.assertEqual(tweet_1.day, 14)
	
    def test_time34(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Caberra", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 8)
		self.assertEqual(tweet_1.day, 14)

    def test_time35(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Kamchatka", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 7)
		self.assertEqual(tweet_1.day, 14)

    def test_time36(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Auckland", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 6)
		self.assertEqual(tweet_1.day, 14)

    def test_time37(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "Wellington", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "PM")
        self.assertEqual(tweet_1.hour, 6)
		self.assertEqual(tweet_1.day, 14)
	
	#changed test format so that it will pass when proper error is thrown.
    def test_time38(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", " ", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
	
    def test_time39(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", " A random zone", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time40(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time41(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "&&&", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time42(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "afjndklnfgsoghdfn", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time43(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "_______", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time44(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "££££££££", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            
    def test_time45(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 12, 00, "PM", "€€€€€€€", 10, 15, "This should pass", "n/a")
        try:
			eastern_std_time = convert_time_zone(tweet_1)
		except CreateTweetError:
			pass
		else:
			self.fail("Did not raise CreateTweetError")
            





if __name__ == '__main__':
    unittest.main()