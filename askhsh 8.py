import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor


consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
api = tweepy.API(auth)

#input tweetsuser1
user1 = raw_input("Give first account name:\n")

#input tweetsuser2
user2 = raw_input("Give second account name:\n")

#insert tweets1 in list
tweetsuser1 = ""
for status in tweepy.Cursor(api.user_timeline, screen_name=user1, tweet_mode='extended').items(10):
    tweetsuser1 = tweetsuser1 + status.full_text + ""

#seperate words1 of tweets
words1 = tweetsuser1.split()
#number of words
counter1 = len(words1)

#get followers1 ammount
data1 = auth_api.get_user(user1)
followers1 = str(data1.followers_count)

#product1 calculation
product1 = int(counter1)*int(followers1)

#insert tweets2 in list
tweetsuser2 = ""
for status in tweepy.Cursor(api.user_timeline, screen_name=user2, tweet_mode='extended').items(10):
    tweetsuser2 = tweetsuser2 + status.full_text + ""

#seperate words2 of tweets
words2 = tweetsuser2.split()
#number of words
counter2 = len(words2)

#get followers2 ammount
data2 = auth_api.get_user(user2)
followers2 = str(data2.followers_count)

#product1 calculation
product2 = int(counter2)*int(followers2)


#check and print results
if product1 > product2:
    print "the user", user1, "has bigger product"
elif product2 > product1:
    print "the user", user2, "has bigger product"
else:
    print "both have same product"
  
