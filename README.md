A Python program using Selenium webdriver API to automate searching for Nintendo Switch availability at Best Buy website.

## Developed and Tested on:

- macOS Mojave **(10.15.4)**
- Python **3.7.2**
- Google Chrome **81.0.4044.138**



## Setup

### Clone repo
```
$ git clone https://github.com/Bramba7/Nintendo-Switch-Buy-best-buy.git
```

### Install Chrome webdriver
- Based on the version of your Chrome, please pick up the relevant chrome webdriver
zip file from here:  
https://sites.google.com/a/chromium.org/chromedriver/downloads

- Unzip and place the binary `chromedriver` in the same directory as the repo

### Install python modules

```
$ pip install selenium
$ pip install PyYAML
```




## Settings
If you are using this program, I assume you already have an BestBuy account,
if not please create one before using this.  

#### BestBuy deails
Please update your BestBuy account details in [settings.yaml](settings.yaml) file in your local copy
- Replace 'UserLogin' with your BestBuy email or username 
- Replace 'Password' with your BestBuy password  



## Run the program
```
$ python3 bot.py
```
The program will run for 8 hours and the page will be checked every 30 seconds, if the product enters the stock. When the product is found to be available for purchase, the program will automatically add it to your shopping cart and an alarm will sound.



## NOTES

When the alarm sounds, you must continue the process to complete the purchase.

