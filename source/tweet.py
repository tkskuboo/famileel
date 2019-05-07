#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs

# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = '0pVW0zBKwThErXWyJDXK6fmpq'
CONSUMER_SECRET = '95KaxKx8j5n0vt3tuKDPAdt2x8ieCLYklMsmi5a1wj3aqTEwWw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '982867513414332416-tKfCNGZevGhQTxtNL3b5YSw97LM3BN4'
ACCESS_SECRET = '8H47XrmJ8PRkb6kfOq6gOEaBTFP9Dv3MaulXePzsgrTWm'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Auth Done!')

# 送信テキストのセット
with open("voice.txt","r") as f:
    l = f.readline()
print("sent")
f.close()

api.update_status(status=l)
