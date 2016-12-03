# ***
# @author BW Babcock
# @description This file constitutes a few tests for the tweet.py file.
# ***

import unittest  # import Python's unittest package.
import sys

sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')
from tweet import create_tweet  # import the class meant to create the tweets for testing.
from error import CreateTweetError  # import my filter file (the file being tested)
from verifytime import convert_time_zone
from verifytime import time_check
import json


class TweetTest(unittest.TestCase):
    # Each function indicates a test case for the tweet.py file.

    def test_tweet1(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertEqual(tested_Tweet.hour, 8)
        self.assertEqual(tested_Tweet.minute, 45)
        self.assertEqual(tested_Tweet.period, "AM")
        self.assertEqual(tested_Tweet.month, 12)
        self.assertEqual(tested_Tweet.day, 26)
        self.assertEqual(tested_Tweet.msg, " Wake up!")


    def test_tweet2(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "false"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet3(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 15/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet4(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : ""}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet4(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 9/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet5(self):
        test_obj = json.loads('{"direct_message" : {"text" : "14:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet6(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 12/54 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet7(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 :  : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet8(self):
        test_obj = json.loads('{"direct_message" : {"text" : "845 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet8(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM :  : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet9(self):
        test_obj = json.loads('{"direct_message" : {"text" : "!@:%^ : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet10(self):
        test_obj = json.loads('{"direct_message" : {"text" : "!@:#$ : () : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet11(self):
        test_obj = json.loads('{"direct_message" : {"text" : " :  :  : !", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet12(self):
        test_obj = json.loads('{"direct_message" : {"text" : "-8:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet13(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:-45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet14(self):
        test_obj = json.loads('{"direct_message" : {"text" : " :  :  : !!!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : ""}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet15(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8:45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "!@#$%^&*("}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet16(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8::45 : AM : 12/26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)

    def test_tweet17(self):
        test_obj = json.loads('{"direct_message" : {"text" : "8_  :  45_ : AM_ : 12  /  _26 : Wake up!", "sender_screen_name" : "myTwitterHandle", "sender" : {"time_zone" : "Atlantic Time (Canada)"}, "recipient" : { "following" : "true"}}}')
        tested_Tweet = create_tweet(test_obj)
        self.assertRaises(CreateTweetError)






if __name__ == '__main__':
    unittest.main()
