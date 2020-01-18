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

    tip = random.choice(tips)

    while True:
        cursor = ''
        response = client.users_list(cursor=cursor).data
        members = response['members']
        user_ids = [member['id'] for member in members]

        for user_id in user_ids:
             client.chat_postMessage(
                channel=user_id,
                text=tip
            )

        cursor = response['response_metadata']['next_cursor']

        if not cursor:
            break


start()
