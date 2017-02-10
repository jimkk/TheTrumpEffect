import twitter
import os
import NLP

api = twitter.Api(consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
                    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
                    access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
                    access_token_secret=os.environ["TWITTER_TOKEN_SECRET"])

api.VerifyCredentials()

donald = api.GetUser(screen_name="realDonaldTrump")

tweets = api.GetUserTimeline(donald.id)
for tweet in tweets:
    print("%s: %s\n%s\n\n" % (tweet.created_at, tweet.text, NLP.getSentiment(tweet.text)))
