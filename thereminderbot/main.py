"""
@author Tyler Lambert
This file sets up the OAuth tokens to allow automated access to TheReminderBot's
Twitter account with Read, Write, and view DM privileges. It then sets up the
userstream that streams any new DMs. When a new DM is received, it is sent to
be parsed to make a Tweet object.
OAuth Tokens: https://apps.twitter.com/
API: https://github.com/sixohsix/twitter/tree/master/twitter
"""


from twitter import TwitterStream, Twitter, OAuth
from tweet import create_tweet
from verifytime import convert_time_zone, time_check
from database import insert_to_database
from filter import filter_tweet


# when repo is made public, the keys and tokens will be replaced with placeholders
# auth = OAuth(
#     consumer_key='2CE1E6U7odFK1MFWeCnOPIh5R',
#     consumer_secret='SqqWIvcMGdLbwAqu2oSBzsCr4379aSITLy4AsA9HZyPQxYqCl6',
#     token='796842527487889409-hY298XB4dZGxBLU2blhpCVMz14UPQo8',
#     token_secret='E9CmwGNpDNffxzU7NjuXernjofYSEF6RyjEKiVantXJap'
# )
auth = OAuth(  # keys for reminderbot002@gmail.com , secondary test account with same login
    consumer_key='PfV0xdYWs55kstAO4PHF1kIHt',
    consumer_secret='wYtyvj7EaHBWftLCR8sfYBJKQISu4PhhWszIuLACo0I4jqBgAi',
    token='792039779068157952-HxKthF9JlcGtDYEiHfT1bn456tJKNLE',
    token_secret='Fl24QTmnau3vQB3svxDBnepwTL4ifGHvLJVD52PXKXh99'
)

t = Twitter(auth=auth)

twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        tweet_obj = create_tweet(msg)
        if tweet_obj is None:
            continue
        else:
            filter_tweet(tweet_obj) # successfully calls error
            convert_time_zone(tweet_obj) # successfully calls some of the errors
            #time_check(tweet_obj) # is not quite working right now
            insert_to_database(tweet_obj)
            print(tweet_obj)
    else:
        print("No new messages.")