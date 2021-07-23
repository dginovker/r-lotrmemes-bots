import time

import praw

smeagol = praw.Reddit("smeagol-bot", user_agent='smeagol lotrmemes quote bot')


def scan_comments():
    try:
        while True:
            for comment in smeagol.subreddit("lotrmemes").stream.comments(skip_existing=True):
                print(comment.body)
    except Exception as e:
        print("Exception caught: ")
        print(e)
        scan_comments()


scan_comments()
