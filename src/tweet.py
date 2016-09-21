"""
@author Tyler Lambert
This Tweet class will make a Tweet object after the createTweet function 
is called. The Tweet object is passed to every function after createTweet
completes.
"""

class Tweet:

	def __init__(self, sender, hour, minute, period, time_zone, month, day, msg):
		self.sender = sender			# the sender's Twitter handle
		self.hour = hour 				# converted to EDT in convertTimeZone
		self.min = minute					# converted to EDT in convertTimeZone
		self.period = period 			# AM or PM
		self.time_zone = time_zone		# will remain unchanged
		self.month = month
		self.day = day
		self.msg = msg 					# will be checked with filter function
		
	def __str__(self):
		return sender + msg