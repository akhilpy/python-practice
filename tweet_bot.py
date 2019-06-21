import tweepy
import json

# Authenticate to Twitter

#  consumer_key = os.getenv("CONSUMER_KEY")
#     consumer_secret = os.getenv("CONSUMER_SECRET")
#     access_token = os.getenv("ACCESS_TOKEN")
#     access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
#auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler("fhfghfh", "ewPQiydTpPUi8LJouY2n3EMaeGNm9yLssx8ILjKJe69nO9Jtbpr")
auth.set_access_token("91530797-GUFCliRpmEHyM1J1hqOFwarIQYnAQgppDt7daK8HKf", "XqWHNYXjygfGKkZ4bGqxF3GBtOSdXsH4mPp0nBrqcy3YSQ")

# Create API object
api = tweepy.API(auth)
# options=dir(api)
# for option in options:
#     print(option)


# Create a tweet
res=api.update_status("Hello This is an automated tweet #Testing")

#Get the Top tweet on time line
timeline = api.home_timeline(count=20)

for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")


tweet = timeline[1]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
res=api.create_favorite(tweet.id)
print(res)


for block in api.blocks():
    print(block.name)

for tweet in api.search(q="Abhinandan", lang="en", rpp=2):
    print(f"{tweet.user.name}:{tweet.text}")

#Get A public account detail
user = api.get_user("akhil_24")

print("User details:")
print(user.name)
print(user.description)
print(user.location)


print(user._json)
for k, v in user._json.items():
    print(k, ":-", v)

print("Last 20 Followers:")
count=1
for follower in user.followers(count=100):
    print(follower.name,":--", follower.screen_name)
    count=count+1

print(count)

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        tweet = json.loads(tweet)
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["modi"], languages=["en"])

tweets = api.mentions_timeline()

for tweet in tweets:
    print(f"Liking tweet {tweet.text} of {tweet.author.name}")
    tweet.favorite()
    tweet.user.follow()
follower = api.followers(count=100)
for f in follower:
    print(f.name,  f.screen_name)
