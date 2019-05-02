import tweepy
import config
import sys


def retweet(arg_tweet_id):
    api = config.get_api()
    tweet = api.get_status(arg_tweet_id)

    try:
        api.retweet(arg_tweet_id)
        print(str(tweet.text) + " retweet completed. \n\n")
    except:
        print(str(tweet.text) + " is aleady retweet.\n\n")


def execute():
    print('====== Enter Retweet Tweet`s id   =====')
    while True:
        tweet_id = ''
        tweet_id = input('>  ')
        if tweet_id and len(str(tweet_id)) == 19:
            # id は基本的に19桁の数字なのでそれ以外は弾く。API仕様が変わったら変更せなあかん
            break
        else:
            print('illegal input value')
    retweet(tweet_id)


if __name__ == '__main__':
    execute()
