#!/usr/bin/python

from twitter import *
from Utils import Files

out = list()
outfile = '/home/vengle/projects/Twitter/Tweets.txt'

config = {}
execfile("/home/vengle/projects/Twitter/config.py", config)

# create twitter API object
twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

# this is the user we're going to query.
user = "realDonaldTrump"
#user = "vfrengle"

# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
results = twitter.statuses.user_timeline(screen_name=user, count=7)

for status in results:
    username = status['user']['screen_name']
    create_date = status["created_at"]
    tweeted =  status["text"].encode("ascii", "ignore")
    out.append(create_date + '| USER=' + username + ' | ' + tweeted + "\n\n")

user = "POTUS"
results = twitter.statuses.user_timeline(screen_name=user, count=7)

for status in results:
    username = status['user']['screen_name']
    create_date = status["created_at"]
    tweeted =  status["text"].encode("ascii", "ignore")
    out.append(create_date + '| USER=' + username + ' | ' + tweeted + "\n\n")


f = Files()
f.write_file_append(outfile,out)








