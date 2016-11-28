from time import localtime, strftime

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

def update_log(user, error):
    f = open('../website/public/log_input.html', 'a')
    time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    tmp_str = "<tr><td>{0} </td><td>{1} </td><td>{2}</td></tr>".format(user, error, time)
    f.write(tmp_str)
    f.close()