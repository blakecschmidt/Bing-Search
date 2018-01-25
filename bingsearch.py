import os
import time
import webbrowser
from random import randint

file = open("words.txt", "r")
words = []
for line in file:
    words.append(line)

for i in range(1, 31):

    idx = randint(0, len(words) - 1)
    search = "What does the word " + words[idx] + " mean?"

    url = 'https://www.bing.com/search?q=' + search

    # Open URL in new browser window
    webbrowser.open_new_tab(url) # opens in default browser

    time.sleep(20)

    if i % 4 == 0:
        time.sleep(30)
        os.system("pkill chromium-browse")
        time.sleep(10)

os.system("pkill chromium-browse")

