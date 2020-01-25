import time as time_
import os
from datetime import datetime

from parser import *
from email import *


def run():
    print("Checking for scheduled notes..")
    ###
    directory = 'notes'

    start_time = time_.time()

    while True:
        print("tick")

        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                file_uri = directory + '/' + filename
                f = open(file_uri)
                content = f.read()

                if has_r(file_uri) and not has_reminder(file_uri):
                    # Show Note #
                    print(content)
                    send_mail(content)

                    # create a reminder
                    now = datetime.now().strftime("%Y-%m-%d %H:%M")
                    dt_str = get_new_reminder(now, get_r(file_uri))

                    set_reminder_datetime(file_uri, dt_str)

                now = datetime.now().strftime("%Y-%m-%d %H:%M")

                if has_r(file_uri) and has_reminder(file_uri) and get_reminder(file_uri) < now:
                    # Show Note #
                    print(content)
                    send_mail(content)

                    dt_str = get_new_reminder(get_reminder(file_uri), get_r(file_uri))
                    set_reminder_datetime(file_uri, dt_str)

                if not has_r(file_uri) and has_reminder(file_uri) and get_reminder(file_uri) < now:
                    ## Show Note ##
                    print(content)
                    send_mail(content)

                continue
            else:
                break

        time_.sleep(60.0 - ((time_.time() - start_time) % 60.0))
    ###

run()
