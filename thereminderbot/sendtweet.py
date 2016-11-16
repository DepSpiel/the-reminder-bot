"""
@author <insert name>
<insert desc>
"""


from main import t

def send_tweet(tweet_obj):
    t.statuses.update(status='@' + tweet_obj.sender + " " + tweet_obj.msg)
    return