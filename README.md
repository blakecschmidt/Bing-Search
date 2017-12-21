# Bing-Search
With these two pieces of code, you can run a daily cron job to max out your daily Bing search engine points for Microsoft Rewards.

Microsoft Rewards (once you've reached level 2) allows you to get 5 points per search with 150 points a day using a desktop browser and 100 points a day using a mobile browser.

<b>bingsearch.py</b> runs searches using your default browser and searches the numers 1 through 30 in order to max out the points.

<b>bingsearchmobile.py</b> does the same thing except with a different browser (with the numbers 31 through 50) in which I could change the User Agent to the iPhone's Safari User Agent so that it thinks I'm viewing from a mobile device.

Because I have these running on a Raspberry Pi Zero running Raspbian Jessie, the best way for me to do the mobile version was to use a browser called Epiphany. You can change this browser to anything you would like as long as you can get it to change to a different User Agent. Also, The reason I have so many <i>time.sleep()</i> lines is because the RPi isn't very powerful and so I needed it to give the computer some time so that it could load the pages. The program also quits every 4 tabs because otherwise the tabs would stop loading.
