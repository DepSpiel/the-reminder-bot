from twitter import *

"""
@author Tyler Lambert
This file sets up the OAuth tokens to allow automated access to TheReminderBot's
Twitter account with Read, Write, and view DM privileges. It then sets up the
userstream that streams any new DMs. When a new DM is received, it is sent to
be parsed to make a Tweet object.
OAuth Tokens: https://apps.twitter.com/
API: https://github.com/sixohsix/twitter/tree/master/twitter
"""

from src.tweet import create_tweet

# when repo is made public, the keys and tokens will be replaced with placeholders
auth = OAuth(
    consumer_key='S0F7lEqtL8vMwaZXhMYKnRCoQ',
    consumer_secret='8WE3PHwcNhSM46Gt0MF5Et1asckLyr6rGhE8yj30e3boJTTCln',
    token='774409787559862272-095bXtGJmQT1tnsOkww88dXPEaIrEwR',
    token_secret='1rwvvZtNnvlcQgkv34q3c7XVPjtvv28IpIlvUS8hAx9XE'
)

t = Twitter(auth=auth)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        tweet_obj = create_tweet(msg)
        if tweet_obj is None:
            continue
        else:
            print(tweet_obj)
    else:
        print('No new messages...')