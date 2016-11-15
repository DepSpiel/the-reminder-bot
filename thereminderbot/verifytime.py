"""
@author <Lacey Perry>
<Time.py provides 2 functions. The first, time_check, will reject any time
already passed to prevent storage of messgaes that can't be sent. The second
function convert_time_zone will take the users time zone and convert
their local time to EDT.>
"""
#note wait for Nov. 6th to make sure DST change doesn't mess this up change
#occurs at 2:00AM

import time
from datetime import datetime, timedelta
from thereminderbot.error import CreateTweetError

#dict of timezones supported by twitter keys are GMT/UTC offset
tzsontwitter={-11:["International Date Line West", "Midway Island",
                       "American Samoa"],
                  -10:["Hawaii"],
                  -8:["Alaska"],
                  -7:["Pacific Time (US & Canada)", "Tijuana", "Arizona"],
                  -6:["Mountain Time (US & Canada)", "Chihuahua", "Mazatlan",
                      "Saskatchewan", "Central America"],
                  -5:["Central Time (US & Canada)", "Guadalajara", "Mexico City"
                      ,"Monterrey", "Bogota", "Lima", "Quito"],
                  -4:["Eastern Time (US & Canada)", "Indiana (East)", "Caracas"
                       , "La Paz", "Georgetown"],
                  -3:["Atlantic Time (Canada)", "Santiago", "Buenos Aires"],
                  -2.5:["Newfoundland"],
                  -2:["Brasilia", "Greenland", "Mid-Atlantic"],
                  -1: ["Cape Verde Is."],
                  0:["Azores", "Monrovia", "UTC"],
                  1:["Dubin", "Edinburgh", "Lisbon", "London", "Casablanca",
                     "West Central Africa"],
                  2:["Belgrade","Bratislava", "Budapest", "Ljubljana", "Prague"
                     , "Sarajevo", "Skopje", "Warsaw", "Zagreb", "Brussels",
                     "Copenhagen", "Madrid", "Paris", "Amsterdam", "Berlin",
                     "Bern", "Rome", "Stockholm", "Vienna", "Cairo", "Harare",
                     "Pretoria"],
                  3:["Bucharest", "Helsinki", "Kiev", "Kyiv", "Riga", "Sofia",
                     "Talinn", "Vilnius", "Athens", "Istanbul", "Minsk",
                     "Jerusalem", "Moscow", "St. Petersburg", "Volgograd",
                     "Kuwait", "Riyadh", "Nairobi", "Baghdad"],
                  3.5:["Tehran"],
                  4:["Abu Dhabi", "Muscat", "Baku", "Tbilisi", "Yerevan"],
                  4.5:["Kabul"],
                  5:["Ekaterinburg", "Islamabad", "Karachi", "Tashkent"],
                  5.5:["Koikata", "Chenmai", "Mumbai", "New Delhi"
                       ,"Sri Jayawardenepura"],
                  5.75:["Kathmandu"],
                  6:["Astana", "Almaty", "Novosibirsk", "Urumqi"],
                  6.5:["Rangoon"],
                  7:["Bangkok", "Hanoi", "Jakarta", "Krasnoyarsk"],
                  8:["Beijing", "Chongqing", "Hong Kong", "Kuala Lumpur",
                     "Singapore", "Taipei", "Perth", "Irkutsk", "Ulaanbaatar"],
                  9:["Seoul", "Osaka", "Sapporo", "Tokyo", "Yakutsk"],
                  9.5:["Darwin"],
                  10:["Brisbane", "Vladivsotok", "Guam", "Port Moresby",
                      "Solomon Is."],
                  10.5:["Adelaide"],
                  11:["Caberra", "Melbourne", "Sydney", "Hobart", "Magadan",
                      "New Caledonia"],
                  12:["Fiji", "Kamchatka", "Marshall Is."],
                  13:["Auckland", "Wellington", "Nuku'alofa"]}

#EDT current time parameters
timeutc= datetime.utcnow()

#check that the requested time has not already passed. This function first
#converts the time to EDT for ease of comparison then compares the timedelta
#of the current time against the time requested by the user. ValueError is
#raise if day is out of range for month or month not in range 1-12. If user
#tries to enter an hour >12 or <0 a ValueError is thrown as well. If period
#is set to AM and user enters hour>12 CreateTweetError is raised
def time_check(tweet_obj):
    #offset required due to DST
    current_time=datetime(timeutc.year, timeutc.month, timeutc.day,
                          timeutc.hour, timeutc.minute, 0)
    current_time-=timedelta(hours=4)

    #convert to EDT for comparison
    convert_time_zone(tweet_obj)
    userhr=tweet_obj.hour
    userperiod=tweet_obj.period
    
    #check for AM period with hour in PM range
    if userperiod=="AM":
        if userhr>12:
            raise CreateTweetError("Hour field can only be 0-12.")
    
    #conversion to 24 hr clock
    if tweet_obj.period=="PM":
        if userhr!=12:
            userhr=12+userhr
    if tweet_obj.period=="AM":
        if userhr==12:
            userhr=0
      
    userdatetime=datetime(timeutc.year, tweet_obj.month, tweet_obj.day,
                 userhr, tweet_obj.minute, 0)

    now=timedelta(days=current_time.day, hours=current_time.hour,
                  minutes=current_time.minute)
    requested=timedelta(days=tweet_obj.day, hours=userhr,
                        minutes=tweet_obj.minute)
  
    #test if they requested a previous month
    if userdatetime.month<current_time.month:
        raise CreateTweetError("Time requested has passed")

    #timedelta check for days,hours,minutes
    if requested<now:
        raise CreateTweetError("Time requested has passed")

    return None

	
#makes use of datetime object to store users requested time, in a 24 hr/day
#format and calculates the difference in their time zone an EDT using a
#timedelta object to handle difference in hours and rollover of day/month/year
def convert_time_zone(tweet_obj):
    edt_offset = -4
    usertz=tweet_obj.time_zone
    userhr=tweet_obj.hour
    userperiod=tweet_obj.period
    
    #check for AM period with hour in PM range
    if userperiod=="AM":
        if userhr>12:
            raise CreateTweetError("Hour field can only be 0-12.")
    
    #conversion to 24 hr clock
    if tweet_obj.period=="PM":
        if userhr!=12:
            userhr=12+userhr
    if tweet_obj.period=="AM":
        if userhr==12:
            userhr=0
    
    userdatetime=datetime(timeutc.year, tweet_obj.month, tweet_obj.day, userhr,
                 tweet_obj.minute, 0)


    #check for user time zone and convert as needed.
    if usertz=="Eastern Time (US & Canada)" or usertz=="Indiana (East)" or \
        usertz=="Caracas" or usertz=="La Paz" or usertz=="Georgetown":
        return None
    else:
        for keys,vals in tzsontwitter.items():
            for x in vals:
                if x==usertz:
                    tempmin=timedelta(minutes=0)
                    #check for 1/2 and 3/4 timezones
                    if keys%1==.5:
                        tempmin=timedelta(minutes=30)
                        
                    if keys%1==.75:
                        tempmin=timedelta(minutes=45)
                        
                    userdatetime+tempmin
                    temphr=timedelta(hours=keys-edt_offset)
                    userdatetime-=temphr
                    break
                
        #convert time back to 12 hr format        
        convert= userdatetime.hour
        if userdatetime.hour>=12:
            convert=userdatetime.hour-12
            tweet_obj.period="PM"
        else:
            tweet_obj.period="AM"

        #convert the tweet_obj fields    
        tweet_obj.month=userdatetime.month
        tweet_obj.day=userdatetime.day
        tweet_obj.hour=convert
        tweet_obj.minute=userdatetime.minute        

    return None			
