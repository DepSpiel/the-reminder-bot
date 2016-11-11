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

import mysql.connector

cnx = mysql.connector.connect(host='127.0.0.1', database='test')
cursor = cnx.cursor()


def insert_to_database(tweet_obj):
    reminder_str = "INSERT INTO REMINDERS (SENDER, HOUR, MINUTE, PERIOD, " \
                   "TIMEZONE, MONTH, DAY, MSG, FOLLOWING) VALUES ('{0}', {1}," \
                   " {2}, '{3}', '{4}', {5}, {6}, '{7}', {8});".format(tweet_obj.sender,
                    tweet_obj.hour, tweet_obj.minute, tweet_obj.period,
                    tweet_obj.timezone, tweet_obj.month, tweet_obj.day, tweet_obj.message,
                    tweet_obj.following)
    cursor.execute(reminder_str)
    cnx.commit()
    return
