import datetime

def get_today_unix_time():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    return int(yesterday.timestamp()) * 1000