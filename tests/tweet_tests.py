# ***
# @author BW Babcock
# @description This file constitutes a few tests for the tweet.py file.
# ***

import unittest  # import Python's unittest package.
import sys

sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')
from tweet import Tweet  # import the class meant to create the tweets for testing.
from tweet import CreateTweetError  # import my filter file (the file being tested)
from verifytime import convert_time_zone
from verifytime import time_check
import json 


class TweetTest(unittest.TestCase):
    # Each function indicates a test case for the filter.py file. This file and the tests within it are based on time_tests_2, with a few additions (testing 'null', etc.)

    def test_tweet1(self):
        test_obj = json.dumps('8:45 : AM : 12/26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self.assertEqual(tested_Tweet.hour, 12)
        self.assertEqual(tested_Tweet.minute, 45)
        self.assertEqual(tested_Tweet.period, "AM")
        self.assertEqual(tested_Tweet.month, "8")
        self.assertEqual(tested_Tweet.day, "26")
        self.assertEqual(tested_Tweet.msg, "Wake up!")


    def test_tweet2(self):
        test_obj = json.dumps('8:45 : AM : 12/26 : Wake up! : Extra Field')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet3(self):
        test_obj = json.dumps('8:45 : AM : 12/26 : Wake up! : Extra Field : Extra Extra Field')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet4(self):
        test_obj = json.dumps('8:45  AM  12/26  Wake up!  Extra Field')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet4(self):
        test_obj = json.dumps('8:45 / AM / 12/26 / Wake up! / Extra Field')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet5(self):
        test_obj = json.dumps('8:45 ::: AM : 12/26 : Wake up! : Extra Field')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet6(self):
        test_obj = json.dumps('::::')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet7(self):
        test_obj = json.dumps('8:45 ::: ')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet8(self):
        test_obj = json.dumps('845 :: AM : 12/26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet8(self):
        test_obj = json.dumps('8:45AM12/26Wake up!Extra Field:::')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet9(self):
        test_obj = json.dumps('8:45AM12::/26Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet10(self):
        test_obj = json.dumps('8:45 : AM : 12/26&& : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet11(self):
        test_obj = json.dumps('8:45 : AM : 12!@#$%^/2 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet12(self):
        test_obj = json.dumps('34:45 : AM : 12/26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet13(self):
        test_obj = json.dumps('34:67 : AM : 12/26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet14(self):
        test_obj = json.dumps('0005:45 : AM : 12/26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet15(self):
        test_obj = json.dumps('10:45_:_AM_:_12/26_:_Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet16(self):
        test_obj = json.dumps('10:45 : AM : 12 26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)

    def test_tweet17(self):
        test_obj = json.dumps('10:45 : AM : 12   /   26 : Wake up!')
        tested_Tweet = create_tweet(test_obj)
        self-assertRaises(CreateTweetError)
  





if __name__ == '__main__':
    unittest.main()