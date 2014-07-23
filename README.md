TweetReadTime
=============

Gets the average data to calculate read time of a tweet

Requres Python 2.7.7 and tweepy libraries.

Tweepy can be downloaded here: http://www.tweepy.org/

You also need to find the User ID of a user on twitter, which can be found here: http://mytwitterid.com/

To use, specify 3 things:
1. Which user you want to collect data for 
2. How long you want to collect data for
3. What time interval you want to use ( >20 seconds)

Note: Twitter rate limits to 180 requests per hour, so use a sampling period of more than 20 seconds to avoid rate limiting. I recommend using 20 or 30 second intervals because they're nice and neat.

Have fun!
