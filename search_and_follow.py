import tweepy
import config
import random

SEARCH_WORD = ['相互', 'Sier']

# 検索した文字列を含むツイートをしたユーザをフォローし、そのツイートをふぁぼするスクリプト


def search_and_follow(arg_search_word):
    if arg_search_word == '':
        # 引数に何も渡されない場合
        word = random.choice(SEARCH_WORD)

    api = config.get_api()

    # 配列を渡すことも出来る
    word = arg_search_word
    set_count = 50
    results = api.search(q=word, count=set_count)

    for result in results:
        username = result.user._json['screen_name']
        user_id = result.id
        print("ユーザーID：" + str(user_id))
        user = result.user.name
        print("ユーザー名：" + user)
        tweet = result.text
        print("ユーザーのコメント：" + tweet)

        try:
            api.create_favorite(user_id)
            api.create_friendship(username)
            print(user + "をフォローと「いいね」をしました\n\n")
        except:
            print(user + "はもうフォローしてます\n\n")


if __name__ == '__main__':
    print('====== Enter Search Word   =====')
    search_word = input('>  ')

    search_and_follow(search_word)
