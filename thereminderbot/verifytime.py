"""
@author <Lacey Perry>
<Time.py provides 2 functions. The first, time_check, will reject any time
already passed to prevent storage of messgaes that can't be sent. The second
function convert_time_zone will take the users time zone and convert
their local time to EDT.>
"""
#note wait for Nov. 6th to make sure DST change doesn't mess this up change
#occurs at 2:00AM

from datetime import datetime, timedelta
from error import CreateTweetError

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

#represent date that time will move forward and fall back in USA
#needs to be changed annually 
dstoff=datetime(timeutc.year, 11, 6, 2,
                 0, 0)
dston=datetime(timeutc.year, 3, 13, 2,
                 0, 0)
"""check that the requested time has not already passed. This function first
converts the time to EDT for ease of comparison then compares the timedelta
of the current time against the time requested by the user. ValueError is
raised if day, month or hour are out of range.index If period is set to AM and
user enters hour>12 CreateTweetError is raised. If time has passed already
this function returns False, otherwise True is returned."""
def time_check(tweet_obj):

    if(tweet_obj == None):
        return False
    if (tweet_obj.month > 12 or tweet_obj.month < 0 ):
        return False
    if (tweet_obj.day > 31 or tweet_obj.day < 0 ):
        return False
    if (tweet_obj.hour > 23 or tweet_obj.hour < 0 ):
        return False
    if (tweet_obj.minute > 59 or tweet_obj.minute < 0 ):
        return False

    #offset required due to DST
    current_time=datetime(timeutc.year, timeutc.month, timeutc.day,
                          timeutc.hour, timeutc.minute, 0)
    current_time-=timedelta(hours=5)

    #convert to EDT for comparison
    convert_time_zone(tweet_obj)
    userhr=tweet_obj.hour
    userperiod=tweet_obj.period
    
    #check for AM period with hour in PM range
    if userperiod=="AM":
        if int(userhr)>12:
            raise CreateTweetError("Hour field can only be 0-12.")
    
    #conversion to 24 hr clock
    if tweet_obj.period=="PM":
        if int(userhr)!=12:
            userhr=12+int(userhr)
    if tweet_obj.period=="AM":
        if int(userhr)==12:
            userhr=0


    userdatetime = datetime(timeutc.year, int(tweet_obj.month), int(tweet_obj.day), int(userhr),
                            int(tweet_obj.minute), 0)


    now=timedelta(days=current_time.day, hours=current_time.hour,
                  minutes=current_time.minute)
    requested=timedelta(days=int(tweet_obj.day), hours=int(userhr),
                        minutes=int(tweet_obj.minute))
  
    #test if they requested a previous month
    if userdatetime.month<current_time.month:
        return False

    #timedelta check for days,hours,minutes
    if requested<now:
        return False

    return True

	
"""makes use of datetime object to store users requested time, in a 24 hr/day
format and calculates the difference in their time zone an EDT using a
timedelta object to handle difference in hours and rollover of day/month/year"""
def convert_time_zone(tweet_obj):

    if (tweet_obj.month > 12 or tweet_obj.month < 0 ):
        return None
    if (tweet_obj.day > 31 or tweet_obj.day < 0 ):
        return None
    if (tweet_obj.hour > 23 or tweet_obj.hour < 0 ):
        return None
    if (tweet_obj.minute > 59 or tweet_obj.minute < 0 ):
        return None

    edt_offset = -4
    usertz=tweet_obj.time_zone
    userhr=tweet_obj.hour
    userperiod=tweet_obj.period
    
    #check for AM period with hour in PM range
    if userperiod=="AM":
        if int(userhr)>12:
            raise CreateTweetError("Hour field can only be 0-12.")
    
    #conversion to 24 hr clock
    if tweet_obj.period=="PM":
        if userhr!=12:
            userhr=int(12+int(userhr))
    if tweet_obj.period=="AM":
        if userhr==12:
            userhr=0

    userdatetime=datetime(timeutc.year, int(tweet_obj.month), int(tweet_obj.day), int(userhr),
                 int(tweet_obj.minute), 0)

    #check for user time zone and convert as needed.
    if usertz=="Eastern Time (US & Canada)" or usertz=="Indiana (East)" or \
        usertz=="Caracas" or usertz=="La Paz" or usertz=="Georgetown":
        return None
    else:
        for keys,vals in tzsontwitter.items():
            for x in vals:
                if x==usertz:
                    tempmin=timedelta(minutes=0)
                    #check for 1/2 and 3/4 timezones and update minutes
                    if keys%1==.5:
                        tempmin=timedelta(minutes=30)
                        
                    if keys%1==.75:
                        tempmin=timedelta(minutes=45)

                    userdatetime+tempmin
                    temphr=timedelta(hours=keys-edt_offset)
                    
                    #check for user requested time happening before
                    #or after dst is off. Adjust based on Timezone
                    #and DST observance.
                    if userdatetime<dstoff:
                        if usertz=="Arizona":
                            temphr=timedelta(hours=keys-edt_offset)
                    if userdatetime>dstoff:
                        if usertz=="Azores" or usertz=="Monrovia" or usertz=="UTC":
                             temphr=timedelta(hours=keys-edt_offset+1)
                        if usertz=="Arizona":
                            temphr=timedelta(hours=keys-edt_offset+1)
                            
                    userdatetime-=temphr             
                    break
        #if hour was not modified after loop throw error as timezone was not listed.
        if userdatetime.hour==tweet_obj.hour:
                    raise CreateTweetError("Your Timezone was not listed in the database")
				
        #convert time back to 12 hr format        
        convert=userdatetime.hour
        if userdatetime.hour>=12:
            convert=userdatetime.hour-12
            tweet_obj.period="PM"
        else:
            if convert==0:
                convert=12
            tweet_obj.period="AM"

        #convert the tweet_obj fields    
        tweet_obj.month=userdatetime.month
        tweet_obj.day=userdatetime.day
        tweet_obj.hour=convert
        tweet_obj.minute=userdatetime.minute        

    return None	