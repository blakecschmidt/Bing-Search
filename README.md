# Bing-Search

With this repo, you can run a daily cron job to max out your daily Bing search engine points for Microsoft Rewards.

Microsoft Rewards (once you've reached level 2) allows you to get 5 points per search with 150 points a day using a desktop browser and 100 points a day using a mobile browser.

<b>bingsearch.py</b> runs searches using your default browser and searches the numers 1 through 30 in order to max out the points.

<b>bingsearchmobile.py</b> does the same thing except with a different browser (with the numbers 31 through 50) in which I could change the User Agent to the iPhone's Safari User Agent so that it thinks I'm viewing from a mobile device.

Because I have these running on a Raspberry Pi Zero running Raspbian Stretch, the best way for me to do the mobile version was to use a browser called Epiphany. You can change this browser to anything you would like as long as you can get it to change to a different User Agent. Also, The reason I have so many `time.sleep()` lines is because the RPi Zero isn't very powerful and so I needed it to give the computer some time so that it could load the pages. The program also quits every 4 tabs because otherwise the tabs would stop loading.

The reason there are bash scripts included is because crontab won't run the Python scripts correctly due to the webbrowser package causing problems due to the script accessing the GUI so I had to wrap the command in a bash script and change the DISPLAY variable. The bash scripts are what will be ran in crontab.

## Setup

These setup instructions are tailored to the Raspberry Pi running Raspbian Stretch, although I'm sure the setup on other systems is near identical.

First, download these files to your computer.

If you're using a Raspberry Pi, Epiphany is the easiest browser to do the mobile searches on. Epiphany comes pre-installed with Raspbian but you'll need to change the User Agent so that it displays the mobile version of Bing.

To change the User Agent for Epiphany to iOS 11 Safari, open up your Terminal and enter the command
`gsettings set org.gnome.Epiphany user-agent "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A356 Safari/604.1"`

Now we need to tell the computer to run our two Python scripts every day, enter this into Terminal:
`crontab -e`

Inside crontab, I have added the two lines seen below to run at 5:00 and 5:30 AM every morning
```
0 5 * * * /full/path/to/directory/bingsearch.sh
30 5 * * * /full/path/to/directory/bingsearchmobile.sh
```

After saving this, the two bash scripts should run at the specified times every morning. You may want to check to make sure the cron job runs correctly by first putting a time thats a minute or two after the current time and wait for it to run and make sure it works. You also need to make sure to log in to your Microsoft Rewards account in Bing for both your primary browser (Chromium on the Pi) as well as Epiphany so that you will redeem points for the searches.
