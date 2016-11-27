class Error(Exception):
   """Base class for other exceptions"""
   pass

class FilterError(Error):
   """Raised when profanity is found in tweet"""
   pass

class CreateTweetError(Error):
   """Raised when DM improperly formatted"""
   pass

class TimePassedError(Error):
   """Raised when reminder set for a past time"""
   pass