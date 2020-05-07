from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
import time
import yaml

################## Settings INFO  #########################
SETTINGS_FILE = "settings.yaml"

cfg = {}
with open(SETTINGS_FILE, "r") as yamlf:
    cfg = yaml.load(yamlf, Loader=yaml.SafeLoader)

################## Open Browser   #########################
OPEN_BROWSER = cfg['OPEN_BROWSER']
CHROMEDRIVER = "./chromedriver"


PRODUCT_SITE = "https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253"
LOGIN_SITE = "https://www.bestbuy.com/login"
BESTBUY_LOGIN = cfg['BESTBUY_LOGIN']
BESTBUY_PASSWD = cfg['BESTBUY_PASSWD']
WAIT_FOR_MAIN_SITE = 5
WAIT_FOR_LOGIN_PAGE = 5
WAIT_FOR_INPUT = 2
WAIT_FOR_LOGGING_IN = 10
WAIT_FOR_NEXT_SHOP = 5
WAIT_FOR_SHOP_LOAD = 10

ROUND_WAIT_TIME = 30  # 30 seg
ROUND_COUNT = 960  # Roughly 8 hours


class BrowseForMe:
    def __init__(self):
        opts = Options()
        if OPEN_BROWSER == 0:
            opts.headless = True
        self.browser = webdriver.Chrome(CHROMEDRIVER, options=opts)

    def check_product(self):
        self.browser.get(PRODUCT_SITE)
        time.sleep(WAIT_FOR_MAIN_SITE)
        try:
            check = self.browser.find_element_by_xpath('//button[contains(.,"Add to Cart")]')
        except NoSuchElementException as exeception:
            return None
        check.click()
        time.sleep(WAIT_FOR_INPUT)

        try:
          go_cart_bt = self.browser.find_element_by_xpath("//span[contains(.,'Go to cart')]")
        except NoSuchElementException as exeception:
            print("Error Go Cart Btn")
            self.close_and_quit()
        go_cart_bt.click()
        time.sleep(WAIT_FOR_LOGIN_PAGE)

        while True:
          os.system("afplay alarm.mp3")

    def login(self):
        self.browser.get(LOGIN_SITE)
        time.sleep(WAIT_FOR_MAIN_SITE)

        try:
          email_field = self.browser.find_element_by_xpath("//input[@type='email']")
        except NoSuchElementException as exeception:
            print("Error Login Email add")
            self.close_and_quit()
        email_field.send_keys(BESTBUY_LOGIN)
        time.sleep(WAIT_FOR_INPUT)

        try:
          passwd_field = self.browser.find_element_by_xpath("//input[@type='password']")
        except NoSuchElementException as exeception:
            print("Error Login pwd add")
            self.close_and_quit()
        passwd_field.send_keys(BESTBUY_PASSWD)
        time.sleep(WAIT_FOR_INPUT)

        try:
          login_bt = self.browser.find_element_by_xpath("//button[@type='submit']")
        except NoSuchElementException as exeception:
            print("Error Login Btn")
            self.close_and_quit()
        login_bt.click()
        time.sleep(WAIT_FOR_LOGGING_IN)


    def loop_check_product(self):

            for round in range(ROUND_COUNT):
                self.check_product()
                print("Round: ", round+1)
                time.sleep(ROUND_WAIT_TIME)




    def close_and_quit(self):
        self.browser.close()
        quit()


if __name__ == '__main__':
    browse = BrowseForMe()
    browse.login()
    browse.loop_check_product()
    browse.close_and_quit()




