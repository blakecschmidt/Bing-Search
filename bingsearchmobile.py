import webbrowser
import time
import os

for i in range(31, 51):
    url = 'https://www.bing.com/search?q=' + str(i)

    controller = webbrowser.get('epiphany')
    controller.open_new_tab(url)

    time.sleep(20)

    if i % 4 == 0:
        time.sleep(20)
        os.system("pkill epiphany-browse")
        time.sleep(10)

os.system("pkill epiphany-browse")
