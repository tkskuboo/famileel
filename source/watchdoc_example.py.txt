#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import subprocess

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

trans_cmd = "sudo python /home/pi/python-docs-samples/speech/cloud-client/transcribe_async.py "
tweet_cmd = "sudo python /home/pi/famileel/tweet.py"

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.wav'):
            print('%s has been created.' % event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.wav'):
            print('%s has been modified.' % event.src_path)
            cmd = trans_cmd + event.src_path
            print(cmd.split())
            res = subprocess.check_call(cmd.split())
        if getext(event.src_path) in ('.txt'):
            print("voice.txt modified")
            cmd = tweet_cmd
            print(cmd.split())
            res = subprocess.check_call(cmd.split())

    def on_deleted(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.wav'):
            print('%s has been deleted.' % event.src_path)

if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler,BASEDIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
