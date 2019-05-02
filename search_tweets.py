import tweepy
import config


def search_tweet(arg_keyword, arg_tweet_num=10):
    consumer_key = config.CONSUMER_KEY
    consumer_secret = config.CONSUMER_SECRET
    access_token_key = config.ACCESS_TOKEN
    access_token_secret = config.ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    word = arg_keyword
    set_count = arg_tweet_num
    results = api.search(q=word, count=set_count)

    for result in results:
        print('****************************')
        username = result.user._json['screen_name']
        user_id = result.id
        time = result.created_at
        # print("ユーザーID：" + str(user_id))
        user = result.user.name
        print("ユーザー名：%s" % user)
        tweet = result.text
        print("ユーザーのコメント：%s " % tweet)
        print('TIME :%s' % time)
        # いいね！の操作　検索にヒットしたユーザを全てフォローする恐ろしい機能
        # try:
        #     api.create_favorite(user_id)
        #     api.create_friendship(username)
        #     print(user + "をフォローと「いいね」をしました\n\n")
        # except:
        #     print(user + "はもうフォローしてます\n\n")

    print('****************************')


if __name__ == '__main__':
    print('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')

    print('====== Enter Get Tweets Numbers   =====')
    tweet_num = input('>  ')

    search_tweet(keyword, tweet_num)
