# Lotrmemes bots

Extremely simple bots for your pleasure on /r/lotrmemes!

### Design

These bots are extremely simple by design so anyone can run them. They use simple programming practices where possible and are available for modification per the [license](https://github.com/dginovker/r-lotrmemes-bots/blob/master/LICENSE) (license TL;DR is you must share the source code of your bot too!).

### Running

1. Download the codebase
2. Create a file called `praw.ini` and fill it out with your Reddit [bot info](https://www.reddit.com/r/redditdev/comments/hasnnc/where_do_i_find_the_reddit_client_id_and_secret/) (should look something like [this](https://i.imgur.com/wCuAGLG.png))
3. Run `pip install -r requirements.txt`
4. Run `python main.py`

That's it!

### Modifying the triggers & responses

Edit the dictionary found on line 3 of main.py. Keep the same format!
