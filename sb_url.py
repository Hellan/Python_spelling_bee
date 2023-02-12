# -*- coding: utf-8 -*-
"""
Preparation for Spelling Bee contest.
Program reads data from a file from the url and checks if input given by the user corresponds to
the meaning of the word

"""
import csv
import random
from urllib.request import Request, urlopen
import requests

url = 'https://files.fm/down.php?i=2abbgr55k'
request_site = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
r = requests.get(url)
webpage = urlopen(request_site, timeout=10).read()
url_content = r.content
csv_file = open('d.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

with open('d.csv', encoding="utf8") as f:
    d = dict(filter(None, csv.reader(f)))

points = 0
playNext = "yes"
tries = 0

random_num = random.randint(0, len(d))
key = list(d)[random_num]
answerComp = d[key]

while (playNext == "yes"):

    if (tries < 3):

        question1 = print(str(random_num + 1) + ":  How is  '" + (list(d)[(random_num)]) + "' in English?")
        answerUser = input("Enter your value: ")
        if (answerUser == answerComp):
            points = points + 1
            print("Bravo, you have " + str(points) + " point(s)")
            playNext = input("Wanna play next?")
            random_num = random.randint(0, len(d))
            key = list(d)[random_num]
            answerComp = d[key]
        else:
            print("Not exactly, try again")
            tries = tries + 1
    else:
        print("The answer is: " + answerComp)
        playNext = input("Wanna play next?")
        tries = 0
        random_num = random.randint(0, len(d))
        key = list(d)[random_num]
        answerComp = d[key]
