import random
import re

import praw

trigger_dictionary = {
    ("hobbits"): ["Stupid, fat hobbit!"],
    ("Po-ta-toes", "taters"): ["Whats taters, precious? What's taters, eh?"],
    ("baggins", "bagginses"): ["SHIIIIIIRE! BAGGINS!"],
}


def find_word_in_text(text, word):
    """
    :param text: The text to search
    :param word: Word to look for in text
    :return: True if the word appears as a word in the text, False otherwise
    """
    return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search(text)


def handle_comment(comment):
    """
    Takes in a comment from lotrmemes subreddit
    Maybe replies to it

    :param comment: PRAW comment object
    """
    for triggers, responses in trigger_dictionary.items():
        for trigger in triggers:
            if find_word_in_text(comment.body, trigger):
                response = random.choice(responses)
                print(comment.author.name + " triggered " + trigger + ". Responding with [" + response + "]!")
                comment.reply(response)
                return  # Don't reply more than once per comment
    print(comment.body + " -- Had no triggers")


def scan_comments():
    """
    Permanently scans for comments in lotrmemes subreddit
    Passes comments it finds to handle_comment
    """
    print("Starting bot!")
    smeagol = praw.Reddit("smeagol-bot", user_agent='smeagol lotrmemes quote bot')
    try:
        for comment in smeagol.subreddit("lotrmemes").stream.comments(skip_existing=True):
            handle_comment(comment)

    except Exception as e:
        print("Exception caught: ")
        print(e)
        scan_comments()

# There's no Bagginses around here. They're all up in Hobbiton.

scan_comments()
