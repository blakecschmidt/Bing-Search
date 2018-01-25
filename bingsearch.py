import os
import time
import webbrowser
import requests
from random import randint

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
words = response.content.splitlines()

for i in range(1, 31):

    idx = randint(0, len(words) - 1)
    search = "What does the word " + words[idx].decode() + " mean?"

    url = 'https://www.bing.com/search?q=' + search

    # Open URL in new browser window
    webbrowser.open_new_tab(url) # opens in default browser

    time.sleep(20)

    if i % 4 == 0:
        time.sleep(30)
        os.system("pkill chromium-browse")
        time.sleep(10)

os.system("pkill chromium-browse")
