import webbrowser
import time
import os

for i in range(1, 31):

    url = 'https://www.bing.com/search?q=' + str(i)
        
    webbrowser.open_new_tab(url)

    time.sleep(20)

    if i % 4 == 0:
        time.sleep(30)
        os.system("pkill chromium-browse")
        time.sleep(10)

os.system("pkill chromium-browse")

