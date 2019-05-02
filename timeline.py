#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import config


def get_timeline(arg_get_num=10):

    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    # タイムライン取得用のURL
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

    # 取得数を設定できる
    params = {'count' : arg_get_num}

    # OAuth で GET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        timeline = json.loads(req.text)
        # 各ツイートの本文を表示
        for tweet in timeline:
            print(tweet['user']['name'] + ' @' + tweet['user']['screen_name'])
            print(tweet['text'])
            print('ID :: ' + str(tweet['id']))
            print(tweet['created_at'])
            # print('screen name : @%s' % (tweet['user']['screen_name']))
            print('*******************************************')

    else:
        # エラーの場合
        print("Error: %d" % req.status_code)


if __name__ == '__main__':
    print('====== 取得するツイートの数を入力して下さい   =====')
    tweet_num = input('>  ')

    get_timeline(tweet_num)
