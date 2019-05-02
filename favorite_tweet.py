import tweepy
import config


def favorite_tweet(arg_id):
    consumer_key = config.CONSUMER_KEY
    consumer_secret = config.CONSUMER_SECRET
    access_token_key = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)
    tweet = api.get_status(arg_id)
    try:
        api.create_favorite(arg_id)
        print(str(tweet.text) + " Favorited Tweets.\n\n")
    except:
        print(str(tweet.text) + " is aleady favorited.\n\n")


if __name__ == '__main__':
    print('====== Enter Favorite Tweet`s id   =====')
    user_id = input('>  ')

    favorite_tweet(user_id)
