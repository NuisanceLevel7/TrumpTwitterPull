#!/usr/bin/python

from twitter import *
from Utils import Files
import time
import sqlite3


tweetdir =  '/home/vengle/projects/Twitter'
conn = sqlite3.connect(tweetdir + '/tweets.db')
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
cur = conn.cursor()


out = list()

outfile = tweetdir + '/tweets_processed'
infile = tweetdir + '/Tweets.txt'


tweetdir2 =  '/home/vengle/projects/TrumpSpeechBot/Speeches'
speechfile = tweetdir2 + '/tweets.txt'

f = Files()
f.read_file(infile)

for line in f.data:
  if 'http' in line:
    pass
  else:
    fields = line.split('|')
    if len(fields) < 3:
      pass
    else:
      tweet_time = fields[0]
      username = fields[1]
      tweettxt = fields[2]
      tweettxt = tweettxt.strip()
      if tweettxt.startswith("\"@") or  tweettxt.startswith("RT "):
        pass
      else:
        cur.execute('''INSERT OR IGNORE INTO TRUMPTWEETER 
                    (id, bstweet)
                    VALUES ( ?,? )''', ( tweet_time, tweettxt ) )



conn.commit()
cur.execute('''SELECT bstweet FROM TRUMPTWEETER''')
for row in cur:
    if len(row[0]) > 15:
        out.append(row[0] + "\n")


f.write_file(outfile,out)
f.write_file(speechfile,out)
f.write_file(infile,['Begin File'])

#
# Schema reference
#
#CREATE TABLE TRUMPTWEETER (
#      id  TEXT NOT NULL PRIMARY KEY UNIQUE,
#      bstweet    BLOB
#);






