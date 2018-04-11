import webbrowser
import time
import os
from random import randint

file = open("words.txt", "r")
words = []
for line in file:
    words.append(line)

for i in range(31, 51):

    idx = randint(0, len(words) - 1)
    search = "How do you pronounce the word " + words[idx] + "?"

    url = 'https://www.bing.com/search?q=' + search

    contr = webbrowser.get('epiphany')
    contr.open_new_tab(url)

    time.sleep(30)

    if i % 4 == 0:
        time.sleep(20)
        os.system("pkill epiphany-browse")
        time.sleep(10)

os.system("pkill epiphany-browse")
