import praw

from reddit import scan_comments

trigger_dictionary = {
    ("hobbits", ): ["Stupid, fat hobbit!"],
    ("Po-ta-toes", "taters", ): ["Whats taters, precious? What's taters, eh?"],
    ("baggins", "bagginses", ): ["SHIIIIIIRE! BAGGINS!"],
    ("pocketses", ): ["What has it got in its pocketses?"],
}

if __name__ == '__main__':
    smeagol = praw.Reddit("smeagol-bot", user_agent='Smeagol lotrmemes quote bot by /u/OsrsNeedsF2P')
    scan_comments(smeagol, trigger_dictionary)
