import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import datetime
import os


#a few things to edit parsing of json code
# I don't think I need it, but I'll keep it for now
@classmethod
def parse(cls, api, raw):
	status = cls.first_parse(api, raw)
	setattr(status, 'json', json.dumps(raw))
	return status

tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse

_dir = os.path.dirname(os.path.abspath(__file__))

#access tokens
ckey  = ''
csecret = ''
atoken = ''
asecret = ''

id_tweet = ""

#Enter twitter ID of user here.
# User: Barack Obama
user_to_follow = "312215961"


#listener class to grab the first thing the user himself tweets
class listener(StreamListener):

    def on_data(self, data):
        try:
            tweet_data = json.loads(data)
            userData = tweet_data["user"]
            if(userData["id_str"] == user_to_follow):
                global id_tweet
                id_tweet = tweet_data["id_str"]
                print id_tweet
                return False
            
            return True
        except BaseException, e:
            print 'failed ondata, ', str(e)
            time.sleep(5)
    def on_error(self, status):
        print status

        

#sets up listener class to wait for a tweet

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream( auth, listener())
twitterStream.filter(follow=[user_to_follow])

api = tweepy.API(auth)
# timing
# to_sample_until - amount of time in seconds
# you want to sample for
# sample_interval - how often you want to sample (seconds)

to_sample_until = 30
sample_interval = 10
i = 0

#make sure tweet is a global variab;e
print "ID: " + id_tweet + " lol"

#delays for a second to make sure 
time.sleep(1)

current_time = str(time.time())

#loop to sample for
while(i < to_sample_until):
        #gets tweet data
        tweet = api.get_status(id_tweet)
        more_data = json.loads(tweet.json)
        rets = str(more_data["retweet_count"])
        favs = str(tweet.favorite_count)
        print "Retweets: " + rets + " Favorites: " + favs
        #writes retweets to file
        retsFile = open('rets_' + str(user_to_follow) +'_' + current_time + '.csv', 'a')
        retsFile.write(rets)
        retsFile.write("\n")
        retsFile.close()
        #writes favorites to a file
        favsFile = open('rets_' + str(user_to_follow) + "_" + current_time + '.csv', 'a')
        favsFile.write(favs)
        favsFile.write("\n")
        favsFile.close()
        #iterates
        time.sleep(sample_interval)
        i = i + sample_interval
        
#done!
print "All done!"

