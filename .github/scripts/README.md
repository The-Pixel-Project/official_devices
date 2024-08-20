# Auto Rom Poster Bot

A simple Post Bot written in [Python]('https://www.python.org') using [pyTelegramBotAPI]('https://pypi.org/project/pyTelegramBotAPI') to post rom updates to telegram channel whenever there is an OTA update.

## Instructions

### 1. Adding secrets

Go to your repo `settings > secrets > new repository secret`, and add these secrets.

- `BOT_TOKEN`: Telegram bot token
- `CHAT_ID`: Telegram group/channel chat ID where the rom needs to be posted
- `BANNER_URL`: Telegraph URL of your rom banner/photo
- `GH_TOKEN`: Github access token to push changes to repo

**Note:** Bot should be added in the group/channel where the rom needs to be posted

### 2. Running the bot

After adding secrets the next thing is to run the bot.

**We use Github Actions to run the bot**

- Actions will automatically run if any changes are committed to the repo and rom will be posted
- You can also run the bot by going to `actions > Rom Poster Bot Runner > workflow-dispatch` and tap on run

## Credits

- [Ashwin DS](https://github.com/geek0609)
