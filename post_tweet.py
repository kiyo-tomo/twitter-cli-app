import json, config # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session # OAuthのライブラリの読み込み
import sys


def post_tweet(arg_post_text):

    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

    url = "https://api.twitter.com/1.1/statuses/update.json"  # ツイートポストエンドポイント

    tweet = arg_post_text

    params = {"status" : tweet}

    res = twitter.post(url, params=params)  # post送信

    if res.status_code == 200:  # 正常投稿出来た場合
        print("Tweet Success.")
    else: # 正常投稿出来なかった場合
        print("Failed. : %d" % res.status_code)


if __name__ == '__main__':

    print("内容を入力してください。'EOF'と入力するまで入力を続けます。")
    post_text = '\n'.join(iter(input, 'EOF'))
    print('*******************************************')
    if len(post_text) > config.MAX_TWEET_LENGTH:
        print("【警告】入力文字数が上限値を超えています。ツイートをキャンセルします。")
        sys.exit()

    while True:
        inp = input('本当に投稿する？ yes/no >>')
        if inp == 'yes' or inp == 'y' or inp == 'Yes' or inp == 'Y':
            break
        if inp == 'no':
            print('ツイートをキャンセル')
            sys.exit()

    post_tweet(post_text)
