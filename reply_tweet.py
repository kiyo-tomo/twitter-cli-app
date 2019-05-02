import tweepy
import config
import sys

# For Test Account
# 1120564669331197952
#
# @kabu_zigen


def reply_tweet(arg_tweet_id, aeg_reply_text):
    api = config.get_api()
    screen_name = get_screen_name(arg_tweet_id)
    status_str = screen_name + ' ' + aeg_reply_text

    api.update_status(
        status=str(status_str),
        in_reply_to_status_id=arg_tweet_id
    )


def get_screen_name(arg_tweet_id):
    api = config.get_api()
    tweet = api.get_status(arg_tweet_id)
    screen_name = '@' + tweet.user.screen_name
    return screen_name


def execute():
    print('====== Enter Reply Tweet`s id   =====')
    while True:
        tweet_id = ''
        tweet_id = input('>  ')
        if tweet_id and len(str(tweet_id)) == 19:
            # id は基本的に19桁の数字なのでそれ以外は弾く。仕様が変わったらどうしよう
            break
        else:
            print('入力値が不正')

    print("リプライする内容を入力してください。'EOF'と入力するまで入力を続けます。")
    rep_text = '\n'.join(iter(input, 'EOF'))
    print('*******************************************')
    if len(rep_text) > config.MAX_TWEET_LENGTH:
        print("【警告】入力文字数が上限値を超えています。リプライをキャンセルします。")
        sys.exit()

    while True:
        inp = input('本当に投稿する？ yes/no >>')
        if inp == 'yes' or inp == 'y' or inp == 'Yes' or inp == 'Y':
            break
        if inp == 'no':
            print('リプライをキャンセル')
            sys.exit()
    reply_tweet(tweet_id, rep_text)
    print('%s にリプライしました。' % get_screen_name(tweet_id))


if __name__ == '__main__':
    execute()
