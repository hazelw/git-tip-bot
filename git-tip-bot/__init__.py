import csv
import json
import os
import random

from slack import WebClient


def start():
    token = os.getenv('GIT_TIP_BOT_TOKEN')
    client = WebClient(token)

    with open('tips.csv') as tips_file:
        tips_reader = csv.reader(tips_file, delimiter='|')
        tips = [tip for (tip,) in tips_reader]

    while True:
        cursor = ''
        conversations = client.conversations_list(
            types='im', cursor=cursor
        ).data

        channel_ids = [
            channel['id'] for channel in conversations['channels']
        ]

        for channel_id in channel_ids:
            tip = random.choice(tips)
            client.chat_postMessage(
                channel=channel_id,
                text=tip
            )

        cursor = conversations['response_metadata']['next_cursor']
        
        if not cursor:
            break


start()
