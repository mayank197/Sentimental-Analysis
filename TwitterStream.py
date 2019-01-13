from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
import json, time
import tkinter
import sentiment_mod as s

ckey = 'TBNl2qxyYjhmWFvjHJ9qNcPg2'
csecret = 'UrySTBYnv5WstfJhR3AttW9Kd7ntEq1CUp7dYNaOaZYtxvoCX1'
atoken = '2955611653-3QgW9Xng08IIJq5jPeJzUStcgcw4XffisNjJzFu'
asecret = 'xRA4SOT0Ipz9z3PWWrno5WmkuzFvoqgKKbFnT3rXTWgWu'

class listener(StreamListener):
    def on_data(self,data):
        all_data = json.loads(data)
        # tweet = all_data["text"]        # error here - solved by changing the code to the below line
        tweet = ascii(all_data["text"])
        username = all_data["user"]["screen_name"]
        
        sentiment_value, confidence = s.sentiment(tweet)
        # print(tweet.encode("utf-8",errors='ignore').decode('utf-8'), sentiment_value, confidence)
        # print(str(tweet,'utf-8'), sentiment_value, confidence)
        print(username,tweet,sentiment_value, confidence)
        # time.sleep(2)
        
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
            
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = API(auth)
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["Hopman Cup","Roger Federer","Serena Williams"])

 
