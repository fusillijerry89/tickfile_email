import re
import random
import datetime
from datetime import *

def has_reminder(file_uri):
    f = open(file_uri, "r")
    content = f.read()

    ### Get repeat days
    r = re.search('{{reminder}}(.+){{reminder}}', content)

    if r:
        return True
    else:
        return False

def has_hour(file_uri):
    f = open(file_uri, "r")
    content = f.read()

    ### Get repeat days
    r = re.search('{{ti}}((\d+)|(\d+,\d+)){{ti}}', content)

    if r:
        return True
    else:
        return False

def has_r(file_uri):
    f = open(file_uri, "r")
    content = f.read()

    ### Get repeat days
    r = re.search('{{r}}((\d+)|(\d+,\d+)){{r}}', content)

    if r:
        return True
    else:
        return False

def get_hour(file_uri):
    f = open(file_uri, "r")
    content = f.read()


    ### Get times of day
    hours = re.search('{{ti}}((\d+)|(\d+,\d+)){{ti}}', content)
    if hours:
        hours = hours.group(1)
        if "," in hours:
            hours = re.search('(\d+),(\d+)', hours)

            lower = int(hours.group(1))
            upper = int(hours.group(2))

            hour = random.randint(lower, upper)

        hour = int(hour)
    else:
        print("No {{ti}} found.")
        hour = None

    return hour


def get_reminder(file_uri):
    f = open(file_uri, "r")
    content = f.read()

    ### Get reminder datetime
    search_str = '{{reminder}}(.+){{reminder}}'

    reminder = re.search(search_str, content)
    if reminder:
        reminder = reminder.group(1)

    if not reminder:
        print("No {{reminder}} found.")
        reminder = None

    return reminder

def get_r(file_uri):
    f = open(file_uri, "r")
    content = f.read()

    ### Get repeat days
    r = re.search('{{r}}((\d+)|(\d+,\d+)){{r}}', content)
    if r:
        r = r.group(1)
        if "," in r:
            r = re.search('(\d+),(\d+)', r)

            lower = int(r.group(1))
            upper = int(r.group(2))

            r = random.randint(lower, upper)

        r = int(r)
    else:
        print("No {{r}} found.")
        r = None

    return r

def set_reminder_datetime(file_uri, dt_str):

    if has_reminder(file_uri):
        f = open(file_uri, "r")
        content = f.read()
        f.close()

        # strip out old datetime and put in new_datetime
        new_reminder_str = '{{reminder}}' + dt_str + '{{reminder}}'

        new_content = re.sub('{{reminder}}(.+){{reminder}}', new_reminder_str, content)

        f = open(file_uri, "w+")
        f.write(new_content)
    else:
        new_reminder_str = '{{reminder}}' + dt_str + '{{reminder}}\n'

        f = open(file_uri, "r")
        content = f.read()
        f.close()

        f = open(file_uri, "w+")
        f.write(new_reminder_str)
        f.write(content)

    f.close()

def update_reminder_datetime(file_uri):
    f = open(file_uri, "r")
    content = f.read()
    f.close()

    reminder_dt = get_reminder_datetime(file_uri)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if reminder_dt < now:
        dt_object = datetime.strptime(reminder_datetime, '%Y-%m-%d %H:%M')
        new_dt = datetime_object + timedelta(days=get_r(file_uri))
        new_dt_str = new_dt.strftime('%Y-%m-%d %H:%M')

        set_reminder_datetime(file_uri, new_dt_str)


def get_new_reminder(old_reminder_dt, r):
    dt_obj = datetime.strptime(old_reminder_dt, '%Y-%m-%d %H:%M')
    r = int(r)

    new_dt = dt_obj + timedelta(days=r)
    new_dt_str = new_dt.strftime('%Y-%m-%d %H:%M')

    return new_dt_str
