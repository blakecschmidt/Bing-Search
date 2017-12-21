import webbrowser
import time

for i in range(0, 30):

    url = 'https://www.bing.com/search?q=' + str(i)

    # Open URL in new browser window
    webbrowser.open_new_tab(url) # opens in default browser

    time.sleep(20)

        

