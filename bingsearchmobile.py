import webbrowser
import time
import os
import requests
from random import randint

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
words = response.content.splitlines()

for i in range(31, 51):

    idx = randint(0, len(words) - 1)
    search = "How do you pronounce the word " + words[idx].decode() + "?"

    url = 'https://www.bing.com/search?q=' + search

    contr = webbrowser.get('epiphany')
    contr.open_new_tab(url)

    time.sleep(20)

    if i % 4 == 0:
        time.sleep(20)
        os.system("pkill epiphany-browse")
        time.sleep(10)

os.system("pkill epiphany-browse")
