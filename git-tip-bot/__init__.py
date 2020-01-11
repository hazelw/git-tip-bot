import os

from slack import WebClient


def start():
    token = os.getenv('GIT_TIP_BOT_TOKEN')
    client = WebClient(token)

    # TODO: how do we send a message to every user that has added the bot
    # to their apps?
    response = client.chat_postMessage(
        channel='#git-tip-bot',
        text='hi from bot'
    )


start()
