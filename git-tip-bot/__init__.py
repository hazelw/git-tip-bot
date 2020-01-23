import schedule
import time

from job import send_tips


schedule.every().day.at('10:00').do(send_tips)


while True:
    schedule.run_pending()
    time.sleep(600)
