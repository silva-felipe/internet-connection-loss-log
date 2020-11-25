import requests
import schedule
import smtplib
from datetime import datetime

log = []


def internet():
    global log
    url = 'https://www.google.com/'  # url to be tested
    timeout = 5
    usr = 'xxxx@gmail.com'  # your email address
    pwd = 'xxxxxxxxxx'  # your email pwd
    data = datetime.today().strftime('%d/%m/%Y - %H:%M:%S')
    try:
        connection = requests.get(url, timeout=timeout)
        if connection and log != []:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            msg = '''Subject: Connection lost\n
Connection lost from {} to {}'''.format(log[0], log[-1])
            server.login(usr, pwd)
            server.sendmail(usr, usr, msg)
            log = []
    except (requests.ConnectionError, requests.Timeout) as exception:
        if exception:
            log.append(data)
            if len(log) == 3:
                log.pop(1)


schedule.every(5).seconds.do(internet)

while __name__ == '__main__':
    schedule.run_pending()
