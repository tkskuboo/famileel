#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs

# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = 'xxx'
CONSUMER_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = 'xxx'
ACCESS_SECRET = 'xxx'
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
