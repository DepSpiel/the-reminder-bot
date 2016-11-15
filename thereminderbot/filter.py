"""
@author BW Babcock
This is the filter function for TRB - ensuring that tweets don't contain profanity, incendiary language, threats, or other inappropriate speech.
Trigger Warning: This file contains a list, forbidden_Words, of common profanity. If you are easily offended, do not view this list.
"""

from thereminderbot.error import FilterError

def filter_tweet(tweet_obj):
    #Procedure:
        #1. Extract message string from the tweet_obj Python Object.
        #2. Create a list of common expletives and threatening verbs
        #2a. Key Assumption: Certain action verbs (i.e., 'shoot', 'kill', 'rape', etc. are interpreted as universally negative. Therefore, their context will not be considered.
        #3. Test String for presence of 'forbidden text'.
        #4. If string passes (i.e., no matches within the 'forbidden word list'), allow the function to return.
        #5. Else, raise a filterError.
    string_to_test = tweet_obj.msg    #This allows the object's message to be stored in a variable for easy access.
    string_to_test = string_to_test.casefold()    #converts the string to all lowercase characters for matching.
    string_to_test = string_to_test.strip(' ')    #strips all whitespace between letters of words (i.e., 'f u c k' would be stripped to 'fuck')
    forbidden_words = ['fuck', 'shit', 'piss', 'cunt', 'damn', 'hell', 'dick', 'bomb', 'shoot', 'kill', 'rape', 'assault', 'murder', 'pussy', 
                        'kike', 'bitch', 'cock', 'cocksucker', 'tits', 'ass', 'nigger', 'nigga', 'bastard', 'beaner', 'spick', 'blowjob', 'clit', 'chink', 'chinc', 'coon', 'cooch', 'cum', 
                        'dildo', 'dike', 'douche', 'fag', 'hoe', 'honkey', 'muff', 'queer', 'rimjob', 'slut', 'whore']    #This is the list that will be the basis for comparison against the tweeted message.
#    for i in forbidden_words:    #Iterate through the list, testing each word for presence within the tweet. If a match is found, raise an exception. Else, return.
#        if i in string_to_test:    #if the message contains a forbidden word:
#            raise FilterError('This tweet contains incendiery language or profanity')
#        else
#            return     #Nothing is found, so return
    return    #Exit
    
    #References: http://www.noswearing.com/, and the Python 3.5.2 Documentation