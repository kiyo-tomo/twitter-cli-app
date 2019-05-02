import tweepy

# Twitter の字数制限を判別する定数。Twitterの仕様変更に対応させる。
MAX_TWEET_LENGTH = 140


 SCREEN_NAME = 'XXXX' # @以下の名前
 # 以下にTwitter APIで取得したトークンを置いておく
 CONSUMER_KEY = 'XXXX'
 CONSUMER_SECRET = 'XXXX'
 ACCESS_TOKEN = 'XXXX'
 ACCESS_TOKEN_SECRET = 'XXXX'

def get_api():
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token_key = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)
    return api
