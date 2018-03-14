import twitter
import random


# Get Twitter Followers

api = twitter.Api(consumer_key='########',
                      consumer_secret='#####',
                      access_token_key='#######',
                      access_token_secret='######')

#print(api.VerifyCredentials())

followers = api.GetFollowers()

# Pick one at random

randomIndex = random.randint(0,len(followers) -1)
randomFollower = followers[randomIndex]
print(randomFollower.screen_name)


# Tweet at the random Followers

tweet = "@{} Hope you are having an amazing day. Keep creating!".format(randomFollower.screen_name)
print(tweet)

status = api.PostUpdate(tweet)
print(tweet)
print("Thanks for tweeting")
