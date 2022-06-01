# Reddit Video Maker Bot 🎥

## Requirements

- Python 3.6+
- Playwright (this should install automatically in installation)

## Installation 👩

1. Clone this repository
2. Rename `.env.template` to `.env` and replace all values with the appropriate fields. To get Reddit keys (**required**), visit [the Reddit Apps page.](https://www.reddit.com/prefs/apps) TL;DR set up an app that is a "script". Copy your keys into the `.env` files.
3. Run `playwright install` and `playwright install-deps`.
4. Run `pip3 install -r requirements.txt`
5. Run `python3 main.py`

## Ways to improve

- [❌] Allowing users to choose a background that is picked instead of the Minecraft one.
- [✅] Allowing users to choose between any subreddit.
- [❌] Allowing users to change voice.
- [✅] Download background progress bar