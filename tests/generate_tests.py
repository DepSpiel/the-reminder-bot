import random, json


# add these to the top of the output file
# import unittest  # import Python's unittest package.
# import sys
#
# sys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')
# from tweet import create_tweet  # import the class meant to create the tweets for testing.
# import json
f = open("create_tweet_tests.py", "w")
f.write("import unittest  # import Python's unittest package.\nimport sys\nsys.path.insert(0, '/home/ubuntu/thereminderbot/thereminderbot')\nfrom tweet import create_tweet\nimport json\n")
f.write("class TweetTest(unittest.TestCase):\n")
i = 0
while(i<5000):
    i += 1
    f.write("    def test_tweet" + str(i) + "(self):\n")
    # p_or_f = random.randint(0,1) # determines if test case will pass or fail
    p_or_f = 1
    if p_or_f == 1: # test case will pass
        # hour
        hour = random.randint(1,12)
        # minute
        minute = random.randint(0,59)
        # period
        period = ''
        am_or_pm = random.randint(0,1)
        if am_or_pm == 1:
            period = "AM"
        if am_or_pm == 0:
            period = "PM"
        # month
        month = random.randint(1,12)
        # day
        day = 0
        if month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
        if month in [4,6,9,11]:
            day = random.randint(1,30)
        if month == 2:
            day = random.randint(1,28)
        # msg
        msg_len = random.randint(1,123)
        msg = ""
        while(msg_len):
            msg_len -= 1
            single_char = chr(random.randint(97,122))
            if single_char in ('\'','\"',"`",".","\\","%"):
                continue
            msg += single_char
        # screen name
        sender = ""
        sender_len = random.randint(1,15)
        while(sender_len):
            sender_len -= 1
            # single_char = chr(random.randint(32,126))
            single_char = chr(random.randint(97,122))
            if single_char in ('\'','\"',"`",".","\\","%"):
                continue
            sender += single_char
        tmp_str = '{\"direct_message\" : {\"text\" : ' + "\"" + str(hour) + ":" + str(minute) + ":" + str(period) + ":" + str(month) + "/" + str(day) + ":" + msg + "\", \"sender_screen_name\" : \"" + sender + "\", \"sender\" : {\"time_zone\" : \"Atlantic Time (Canada)\"}, \"recipient\" : { \"following\" : true}}}"
        f.write("        test_obj = json.loads(\'" + tmp_str + "\')\n")
        f.write("        tested_Tweet = create_tweet(test_obj)\n")
        f.write("        self.assertEqual(tested_Tweet.hour, "+str(hour)+")\n")
        f.write("        self.assertEqual(tested_Tweet.minute, "+str(minute)+")\n")
        f.write("        self.assertEqual(tested_Tweet.period, '"+str(period)+"')\n")
        f.write("        self.assertEqual(tested_Tweet.month, "+str(month)+")\n")
        f.write("        self.assertEqual(tested_Tweet.day, "+str(day)+")\n")
        f.write("        self.assertEqual(tested_Tweet.msg, '"+msg+"')\n")
        f.write("        self.assertEqual(tested_Tweet.sender, '"+sender+"')\n")
    if p_or_f == 0: # test case will fail
        # hour
        hour = random.randint(1,12)
        # minute
        minute = random.randint(0,59)
        # period
        period = ''
        am_or_pm = random.randint(0,1)
        if am_or_pm == 1:
            period = "AM"
        if am_or_pm == 0:
            period = "PM"
        # month
        month = random.randint(1,12)
        # day
        day = 0
        if month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
        if month in [4,6,9,11]:
            day = random.randint(1,30)
        if month == 2:
            day = random.randint(1,28)
        # msg
        msg_len = random.randint(1,123)
        msg = ""
        while(msg_len):
            msg_len -= 1
            single_char = chr(random.randint(32,126))
            if single_char in ('\'','\"',"`",".","\\","%"):
                continue
            msg += single_char
        # screen name
        sender = ""
        sender_len = random.randint(1,15)
        while(sender_len):
            sender_len -= 1
            single_char = chr(random.randint(32,126))
            if single_char in ('\'','\"',"`",".","\\","%"):
                continue
            sender += single_char
        tmp_str = '{\"direct_message\" : {\"text\" : ' + "\"" + str(hour) + ":" + str(minute) + ":" + str(period) + ":" + str(month) + "/" + str(day) + ":" + msg + "\", \"sender_screen_name\" : \"" + sender + "\", \"sender\" : {\"time_zone\" : \"Atlantic Time (Canada)\"}, \"recipient\" : { \"following\" : true}}}"
        f.write("        test_obj = json.loads(\'" + tmp_str + "\')\n")
        f.write("        tested_Tweet = create_tweet(test_obj)\n")
        f.write("        self.assertEqual(tested_Tweet, None)\n")

f.write("if __name__ == '__main__':\n    unittest.main()\n")
f.close()
