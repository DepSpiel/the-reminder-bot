"""
@author Tyler Lambert
Inserts a tweet_obj into the MySQL database.
To config the database:
    > CREATE TABLE reminders(
    -> sender varchar(15) NOT NULL,
    -> hour INT NOT NULL,
    -> minute INT NOT NULL,
    -> period varchar(4) NOT NULL,
    -> time_zone varchar(20) NOT NULL,
    -> month tinyint NOT NULL,
    -> day tinyint NOT NULL,
    -> msg varchar(123) NOT NULL,
    -> following bit NOT NULL);
"""

import pymysql
from twitter import Twitter, OAuth
from datetime import *
import time


def insert_to_database(tweet_obj):
    conn = pymysql.connect(host='localhost', user='root', passwd='thisisthepassword', db='thereminderbot')
    cursor = conn.cursor()
    reminder_str = "INSERT INTO reminders (SENDER, HOUR, MINUTE, PERIOD, " \
                   "TIME_ZONE, MONTH, DAY, MSG, FOLLOWING) VALUES ('{0}', {1}," \
                   " {2}, '{3}', '{4}', {5}, {6}, '{7}', {8});".format(tweet_obj.sender,
                    tweet_obj.hour, tweet_obj.minute, tweet_obj.period,
                    tweet_obj.time_zone, tweet_obj.month, tweet_obj.day, tweet_obj.msg,
                    tweet_obj.following)
    cursor.execute(reminder_str)
    conn.commit()
    cursor.close()
    conn.close()
    return

auth = OAuth(  # keys for reminderbot002@gmail.com , secondary test account with same login
    consumer_key='PfV0xdYWs55kstAO4PHF1kIHt',
    consumer_secret='wYtyvj7EaHBWftLCR8sfYBJKQISu4PhhWszIuLACo0I4jqBgAi',
    token='792039779068157952-HxKthF9JlcGtDYEiHfT1bn456tJKNLE',
    token_secret='Fl24QTmnau3vQB3svxDBnepwTL4ifGHvLJVD52PXKXh99'
)

t = Twitter(auth=auth)

while (1<2):
    conn = pymysql.connect(host='localhost', user='root', passwd='thisisthepassword', db='thereminderbot')
    cursor = conn.cursor()
    # query for selecting ALL table records
    query = ("SELECT SENDER, HOUR, MINUTE, PERIOD, TIME_ZONE, MONTH, DAY, MSG, FOLLOWING FROM reminders ")
    # cursor is now full table
    cursor.execute(query)
    print("Checking DB...")
    # for every element in table, do any of the times match
    # if they do, send tweet to user with message
    prev_string = ''
    for (SENDER, HOUR, MINUTE, PERIOD, TIME_ZONE, MONTH, DAY, MSG, FOLLOWING) in cursor:

        tweet_string = "Hey @" + SENDER + ", " + MSG
        timeutc = datetime.utcnow()
        current_time = datetime(timeutc.year, timeutc.month, timeutc.day-1, timeutc.hour+7, timeutc.minute, 0)
        #print(current_time)
        #print("HOUR:"+str(HOUR)+", MIN: "+str(MINUTE)+", MONTH:"+str(MONTH)+", DAY: "+str(DAY))
        if MONTH == timeutc.month and DAY == current_time.day and HOUR == current_time.hour and MINUTE == timeutc.minute:
            print("SENDER: {0}, HOUR: {1}, MINUTE: {2}, PERIOD: {3}, TIME_ZONE: {4}, MONTH: {5}, DAY: {6}, MSG: {7}, FOLLOWING: {8}".format(SENDER, HOUR, MINUTE, PERIOD, TIME_ZONE, MONTH, DAY, MSG, FOLLOWING))
            t.statuses.update(status=str(tweet_string))
            time.sleep(2.0) #wait two seconds so we don't send out a million tweets at once
            continue

    time.sleep(60.0)
    conn.close()
    cursor.close()