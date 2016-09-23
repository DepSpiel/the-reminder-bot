"""
@author Tyler Lambert
This Tweet class will make a Tweet object after the create_tweet function
is called. The create_tweet function parses the json object to extract the
required fields to make a Tweet object. The Tweet object is created and
passed to every function after create_tweet completes.
"""


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

    def __str__(self):
        return self.sender + ' ' + self.msg


def create_tweet(json_obj):
    # insert code
    return