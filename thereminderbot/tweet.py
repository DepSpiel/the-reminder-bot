"""
@author Tyler Lambert
This Tweet class will make a Tweet object after the create_tweet function
is called. The create_tweet function parses the json object to extract the
required fields to make a Tweet object. The Tweet object is created and
passed to every function after create_tweet completes.
"""

from error import update_log

class Tweet:

    def __init__(self, sender, hour, minute, period, time_zone, month, day, msg, following):
        self.sender = sender			# the sender's Twitter handle
        self.hour = hour 				# converted to EDT in convertTimeZone
        self.minute = minute			# converted to EDT in convertTimeZone
        self.period = period 			# AM or PM
        self.time_zone = time_zone		# will remain unchanged
        self.month = month
        self.day = day
        self.msg = msg 					# will be checked with filter function
        self.following = following		# boolean value determining if user is a follower

    def __repr__(self):
        return str(self.sender) + ' ' + str(self.hour) + ' ' + str(self.minute) + ' ' + str(self.period) + ' ' + \
               str(self.time_zone) + ' ' + str(self.month) + ' ' + str(self.day) + ' ' + str(self.msg)


def create_tweet(json_obj):

    # get the text field of the DM and split the string with ':'
    dm_msg = json_obj['direct_message']['text']
    split_dm_msg = dm_msg.split(':', 4)
    if len(split_dm_msg) != 5:
        update_log("Console", "Too many input fields (':')")
        print("0\n")
        return None

    # set variables from the split text field of the DM
    hour = split_dm_msg[0].replace(" ", "")
    minute = split_dm_msg[1].replace(" ", "")
    period = split_dm_msg[2].replace(" ", "")
    month = split_dm_msg[3].replace(" ", "").split('/')[0].replace(" ", "")
    day = split_dm_msg[3].replace(" ", "").split('/')[1].replace(" ", "")
    msg = split_dm_msg[4]
    try:
        hour = int(hour)
        minute = int(minute)
        month = int(month)
        day = int(day)
    except ValueError as e:
        update_log("Console", "Value error in tweet obj")
        print("Value Error\n")
        return None
    except:
        update_log("Console", "Misc input error in tweet obj")
        print("Misc Input\n")
        return None


    # get the Twitter handle of the sender
    sender = json_obj['direct_message']['sender_screen_name']
    if sender is None:
        update_log("Console", "Sender handle returned as null")
        print("Sender handle null\n")
        return None

    # get the sender's time zone
    time_zone = json_obj['direct_message']['sender']['time_zone']
    if time_zone is None:
        update_log("Console", "User timezone not configured")
        print("User timezone not configured\n")
        return None

    # check to see if sender is following @thereminderbot
    following = json_obj['direct_message']['recipient']['following']
    if following == "false":
        update_log("Console", "Sender not following")
        print("Sender not following\n")
        return None

    # create the Tweet object and return
    tweet_obj = Tweet(sender, hour, minute, period, time_zone, month, day, msg, following)
    return tweet_obj
