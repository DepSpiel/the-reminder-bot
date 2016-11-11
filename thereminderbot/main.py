"""
@author Tyler Lambert
This file sets up the OAuth tokens to allow automated access to TheReminderBot's
Twitter account with Read, Write, and view DM privileges. It then sets up the
userstream that streams any new DMs. When a new DM is received, it is sent to
be parsed to make a Tweet object.
OAuth Tokens: https://apps.twitter.com/
API: https://github.com/sixohsix/twitter/tree/master/twitter
"""


from thereminderbot.twitter import TwitterStream, Twitter, OAuth
from thereminderbot.tweet import create_tweet


# when repo is made public, the keys and tokens will be replaced with placeholders
auth = OAuth(
    consumer_key='2CE1E6U7odFK1MFWeCnOPIh5R',
    consumer_secret='SqqWIvcMGdLbwAqu2oSBzsCr4379aSITLy4AsA9HZyPQxYqCl6',
    token='796842527487889409-hY298XB4dZGxBLU2blhpCVMz14UPQo8',
    token_secret='E9CmwGNpDNffxzU7NjuXernjofYSEF6RyjEKiVantXJap'
)

t = Twitter(auth=auth)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        tweet_obj = create_tweet(msg)
        if tweet_obj is None:
            continue
        else:
            # t.statuses.update(status='@' + tweet_obj.sender + " " + tweet_obj.msg)
            print(tweet_obj)
    else:
        print('No new messages...')