import random
import re

import praw

trigger_dictionary = {
    ("hobbits", ): ["Stupid, fat hobbit!"],
    ("Po-ta-toes", "taters", ): ["Whats taters, precious? What's taters, eh?"],
    ("baggins", "bagginses", ): ["SHIIIIIIRE! BAGGINS!"],
    ("pocketses", ): ["What has it got in its pocketses?"],
}

ignore_authors = {"smeagol-bot", }


def find_word_in_text(text, word):
    """
    Finds if a word is within a text

    :param text: The text to search
    :param word: Word to look for in text
    :return: True if the word appears as a word in the text, False otherwise
    """
    found = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search(text)
    if found:
        return True
    return False


def get_comment_reply(text):
    """
    Takes the text of a comment, determines which reply to use for it

    :param text: Reddit comment text
    :return: String containing comment to reply with, None if no comment is applicable
    """
    for triggers, responses in trigger_dictionary.items():  # For every case in trigger_dictionary
        for trigger in triggers:  # For each string in the cases
            if find_word_in_text(text, trigger):  # If the Reddit comment contains the string
                return random.choice(responses)  # Return a random string that corresponds to the matched tuple


def handle_comment(comment):
    """
    Takes in a comment from lotrmemes subreddit
    Maybe replies to it

    :param comment: PRAW comment object
    """

    if comment.author.name in ignore_authors:
        return  # Don't reply to any comment made by someone in ignore_authors

    reply = get_comment_reply(comment.body)
    if reply is not None:  # If we found a reply for the comment
        comment.reply(reply)


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


if __name__ == '__main__':
    scan_comments()
