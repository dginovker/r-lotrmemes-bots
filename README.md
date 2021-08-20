# Lotrmemes bots

![](https://i.imgur.com/OmC1fEK.png)

Extremely simple bot that replies when some comment has a keyword!

### Request a feature

Want to add quotes? Want a new character? Create an [issue](https://github.com/dginovker/r-lotrmemes-bots/issues) on Github or message me on [Reddit](https://www.reddit.com/user/OsrsNeedsF2P/)!

### Design

These bots are extremely simple by design so anyone can run them. The [license](https://github.com/dginovker/r-lotrmemes-bots/blob/master/LICENSE) allows free use of the code is you likewise share the source code.

### Running

1. Download the codebase
2. Create a file called `praw.ini` and fill it out with your Reddit [bot info](https://www.reddit.com/r/redditdev/comments/hasnnc/where_do_i_find_the_reddit_client_id_and_secret/) (should look something like [this](https://i.imgur.com/wCuAGLG.png))
3. Run `pip install -r requirements.txt`
4. Run `python main.py`

That's it!

### Modifying the triggers & responses

Edit the dictionary found at the top of the relevant bot file. Keep the same format!
