import os
import sys
import time
import webbrowser
import wikipedia
from random import randint


def desktop_browser():
    for i in range(0, 30):

        url = f"https://www.bing.com/search?q={wikipedia.random()}"

        # Open URL in new browser window
        webbrowser.open_new_tab(url)  # opens in default browser

        delay = randint(10, 60)
        time.sleep(10)

        if i % 4 == 0:
            os.system("killall chromium-browser")
            time.sleep(10)

    os.system("killall chromium-browser")


def mobile_browser():
    for i in range(0, 20):

        url = f"https://www.bing.com/search?q={wikipedia.random()}"

        contr = webbrowser.get('epiphany')
        contr.open_new(url)

        delay = randint(10, 60)
        time.sleep(10)

        if i % 4 == 0:
            os.system("killall epiphany")
            time.sleep(10)

    os.system("killall epiphany")


if __name__ == "__main__":
    input = sys.argv[1]

    if input == "desktop":
        desktop_browser()
    elif input == "mobile":
        mobile_browser()
    else:
        print("Don't understand input")
