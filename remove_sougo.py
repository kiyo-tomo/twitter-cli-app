#! /usr/bin/python
import tweepy
import time
import config

# フォロー解除する数を入力。50だとアクセストークンを削除されるので、適当な数字を入れる必要がある。
REMOVE_NUMBER = 25


def get_api():
    api = config.get_api()
    screen_name = config.SCREEN_NAME
    return api, screen_name


def unfollow(api, followers, friends):
    unfollow_cnt = 0
    for f in friends:
        if f not in followers:
            if unfollow_cnt <= REMOVE_NUMBER:
                api.destroy_friendship(f)
                print("{0}のフォローを解除しました。".format(api.get_user(f).screen_name))
                time.sleep(10)
                unfollow_cnt += 1
            else:
                print('一度に解除可能な人数(50人)に達したため処理を中断します。')
                break
    return unfollow_cnt


def follow(api, followers, friends):
    follow_cnt = 0
    for followerId in followers:
        count = 0
        for friendId in friends:
            if followerId == friendId:
                break
            count += 1
        if count == len(friends):
            try:
                api.create_friendship(followerId, True)
                print("ID:{0}をフォローしました。".format(api.get_user(followerId).screen_name))
                time.sleep(10)
                follow_cnt += 1
            except tweepy.error.TweepError:
                print('フォローが失敗しました。')
    return follow_cnt


def yes_no_input(choice):
    while True:
        if choice in ['y', 'Y']:
            return True
        else:
            return False


if __name__ == "__main__":
    u_cnt = 0
    f_cnt = 0
    api, SCREEN_NAME = get_api()
    followers = api.followers_ids(SCREEN_NAME)
    friends = api.friends_ids(SCREEN_NAME)
    choice = input("フォロー解除を実行しますか? [y/N]: ").lower()
    if yes_no_input(choice):
        u_cnt = unfollow(api, followers, friends)
    choice = input("フォローを実行しますか? [y/N]: ").lower()
    if yes_no_input(choice):
        f_cnt = follow(api, followers, friends)
    print('{}人をフォロー解除、{}人をフォローしました。'.format(u_cnt, f_cnt))
    input()