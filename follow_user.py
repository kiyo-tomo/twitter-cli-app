import tweepy
import config
import sys
import argparse


def get_arg():
    parser = argparse.ArgumentParser(
        prog='follow',  # プログラム名
        usage='follow',  # プログラムの利用方法
        description='description',  # 引数のヘルプの前に表示
        epilog='end',  # 引数のヘルプの後で表示
        add_help=True,  # -h/–help オプションの追加
    )

    parser.add_argument('-r', '--remove', help='select mode',
                        action='store_true')
    args = parser.parse_args()
    return args


def follow(arg_user_id):
    api = config.get_api()
    user = api.get_user(arg_user_id).name

    api.create_friendship(arg_user_id)
    print(user + " をFollowしました\n\n")


def destroy_follow(arg_user_id):
    api = config.get_api()
    user = api.get_user(arg_user_id).name

    api.destroy_friendship(arg_user_id)
    print(user + " のフォローを解除しまいした\n\n")


def execute():
    args = get_arg()

    print("====== Enter Follow User's user_i or screen_name or id   =====")
    while True:
        user_id = ''
        user_id = input('>  ')
        if user_id:
            break
        else:
            print('入力値が不正')

    if args.remove:
        # destroy_friendship
        destroy_follow(user_id)
    else:
        # follow
        follow(user_id)


if __name__ == '__main__':
    execute()

