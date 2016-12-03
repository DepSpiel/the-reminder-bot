# ***
# @author BW Babcock
# @description This file constitutes a few more (obscure time zone) tests for the verifytime.py file.
# ***

import unittest  # import Python's unittest package.
import sys

sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')
from tweet import Tweet  # import the class meant to create the tweets for testing.
from error import CreateTweetError  # import my filter file (the file being tested)
from verifytime import convert_time_zone
from verifytime import time_check


class TimeTest2(unittest.TestCase):
    # Each function indicates a test case for the filter.py file.

    def test_time1(self):  # This test should pass, and is meant to establish a baseline.
        tweet_1 = Tweet("@trapkingwillie", 1, 12, "PM", "Copenhagen", 10, 15, "This should pass", "n/a")
        eastern_std_time = convert_time_zone(tweet_1)
        self.assertEqual(tweet_1.period, "AM")
        self.assertEqual(tweet_1.hour, 7)

    #test DST is on and time difference is correct
    def test_time2(self):  # This test should raise a FilterError.
        tweet_2 = Tweet("@trapkingwillie", 1, 12, "PM", "UTC", 10, 15, "Hope this works", "n/a")
        eastern_std_time = convert_time_zone(tweet_2)
        self.assertEqual(tweet_2.period, "AM")
        self.assertEqual(tweet_2.hour, 9)

    #test DST is off and time difference is correect
    def test_time2A(self):  # This test should raise a FilterError.
        tweet_2 = Tweet("@trapkingwillie", 1, 12, "PM", "UTC", 11, 15, "Hope this works", "n/a")
        eastern_std_time = convert_time_zone(tweet_2)
        self.assertEqual(tweet_2.period, "AM")
        self.assertEqual(tweet_2.hour, 8)

    def test_time3(self):  # This test should raise a FilterError.
        tweet_3 = Tweet("@trapkingwillie", 1, 00, "PM", "Darwin", 10, 15, "Why is Brendan coding?", "n/a")
        eastern_std_time = convert_time_zone(tweet_3)
        self.assertEqual(tweet_3.period, "PM")
        self.assertEqual(tweet_3.hour, 11)

    def test_time4(self):  # This test should raise a FilterError.
        tweet_4 = Tweet("@trapkingwillie", 1, 12, "PM", "Bern", 10, 15, "...this is dangerous", "n/a")
        eastern_std_time = convert_time_zone(tweet_4)
        self.assertEqual(tweet_4.period, "AM")
        self.assertEqual(tweet_4.hour, 7)

    #test that day hour and period are correct
    def test_time5(self):  # This test should raise a FilterError.
        tweet_5 = Tweet("@trapkingwillie", 1, 12, "PM", "Fiji", 10, 15, "...tests for Harambe", "n/a")
        eastern_std_time = convert_time_zone(tweet_5)
        self.assertEqual(tweet_5.period, "PM")
        self.assertEqual(tweet_5.day, 14)
        self.assertEqual(tweet_5.hour, 9)

    def test_time6(self):  # This test should raise a FilterError.
        tweet_6 = Tweet("@trapkingwillie", 1, 12, "PM", "Nuku'alofa", 10, 15, "#Trump2016", "n/a")
        eastern_std_time = convert_time_zone(tweet_6)
        self.assertEqual(tweet_6.period, "PM")
        self.assertEqual(tweet_6.hour, 8)

if __name__ == '__main__':
    unittest.main()
