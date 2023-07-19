# simple toolset for web scraping 
# Author : Kilian K.
# useragents, chrome driver, logger, proxy connect

import logging

import undetected_chromedriver as uc

from random import randint

User_Agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    ]

class ScraperTools():

    def Tools_Logger():
        logging.basicConfig(filename='scraper.log', level=logging.DEBUG)
        logging.info('Logging started')

        return logging

    def get_random_userAgent():
        # returns random User Agent from the User_Agents Array

        return User_Agents[randint(0, (len(User_Agents) -1))]

    def webdriver(useragent :str, proxy :str, icognito :bool, headless :bool):

        gchrome = uc.ChromeOptions()
        
        gchrome.add_argument("--start-maximized")
        gchrome.add_argument("--no-sandbox")
        gchrome.add_argument("--disable-setuid-sandbox")

        if useragent is None:
            useragent = ScraperTools.get_random_userAgent
            gchrome.add_argument(f'user-agent={useragent}')

            logging.info(f'no User Agent was given. using : {useragent}')

        if headless is True:
            gchrome.add_argument('--headless')

        if icognito is True:
            gchrome.add_argument('--icognito')
