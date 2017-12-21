import webbrowser
import time

for i in range(31, 51):
    url = 'https://www.bing.com/search?q=' + str(i)
    #headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1'}

    controller = webbrowser.get('epiphany')
    controller.open_new_tab(url)

    time.sleep(20)
