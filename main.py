import datetime
import random
import time
from datetime import date
import os

import random
import time


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


def message():
    date = f'Contribution: {random_date("1/1/2008 1:30 PM", "1/1/2021 4:50 AM", random.random()).replace("AM","").replace("PM","").replace(":","").replace("/","")}'
    return date


def runCmd(cmd):
    stream = os.popen(cmd)
    output = stream.read()
    print(output)


def randomSleep():
    time.sleep(random.uniform(0, 3))


def createFile():
    try:
        f = open(f"dataset/testOne.txt", "w", encoding='utf-8')
        f.write(str(random.randint(0, 100000)) + " hh " + str(random.randint(0, 100000)))
        f.close()
        print("file : ", f"./dataset/testOne.txt", "created")
    except Exception as e:
        print(e)


def createCommit():
    createFile()
    # randomSleep()
    runCmd("git add dataset/testOne.txt")
    m = message()
    runCmd(f"git commit -m 'newupdate'")
    print(f"git commit -m 'newupdate'")
    runCmd('git push')
    # randomSleep()


if __name__ == '__main__':
    for i in range(0, 100):
        createCommit()
