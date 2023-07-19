# author : Kilian K.
# source : https://github.com/Kilixn

import os
import random
import sys
import time
import re
import chromedriver_autoinstaller
import argparse
from tools import ScraperTools

import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
#from xvfbwrapper import Xvfb

class YouTubeBot:
    def uploadBot(video, debug):
      #chromedriver_autoinstaller.install()

      #vdisplay = Xvfb(width=900, height=740)
      #vdisplay.start()
      time.sleep(2)

      #LOGIN into YouTube
      username = 'user@gmail.com' # enter your google mail
      password = 'password' # enter your google password
      user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"

      #setting browser up
      options = uc.ChromeOptions()
      # options.headless = True
      options.add_argument("--log-level=3")
      options.add_argument(f'user-agent={user_agent}')
      # options.add_argument("--window-size=1920,1080")
      # options.add_argument('--ignore-certificate-errors')
      # options.add_argument('--allow-running-insecure-content')
      # options.add_argument("--disable-extensions")
      # options.add_argument("--proxy-server='direct://'")
      # options.add_argument("--proxy-bypass-list=*")
      options.add_argument("--start-maximized")
      options.add_argument("--no-sandbox")
      options.add_argument("--disable-setuid-sandbox")
      options.add_argument("--headless")
     # options.add_argument('--disable-gpu')
     # options.add_argument('--disable-dev-shm-usage')
    #  options.add_argument('--no-sandbox')
      
      # options.binary_location = '/usr/bin/brave'

      bot = uc.Chrome(options=options) 

      bot.get('https://studio.youtube.com/')
      
      time.sleep(random.randint(1, 3))
      
      if debug is True:
        bot.get_screenshot_as_file('screenshots/username_btn.png')
      
      # insert youtube username
      username_btn = bot.find_element(By.XPATH ,'//*[@id="identifierId"]')
      username_btn.click()
      username_btn.send_keys(username)
      ##time.sleep(random.randint(1, 3))
      if debug is True:
        bot.get_screenshot_as_file('screenshots/pwd.png')
      
      bot.find_element(By.XPATH ,'//button[normalize-space()="next-button"]').click()
      time.sleep(random.randint(2, 3))

      #insert youtube password
      if debug is True:
        bot.get_screenshot_as_file('screenshots/password_btn.png')
      
      password_btn = bot.find_element(By.XPATH ,'//*[@id="password"]/div[1]/div/div[1]/input')
      password_btn.click()
      password_btn.send_keys(password)
      ##time.sleep(random.randint(1, 2))
      bot.find_element(By.XPATH ,'//button[normalize-space()="next-button"]').click()
      time.sleep(random.randint(1, 4))

      #upload video
      bot.find_element(By.XPATH, '//*[@id="upload-icon"]').click()

      time.sleep(random.randint(1, 4))
      file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
      file_input.send_keys(video)

      time.sleep(random.randint(2, 4))

      if debug is True:
        bot.get_screenshot_as_file('screenshots/find_next.png')
      
      for i in range(3):
          if i == 0:
              time.sleep(3)
              if debug is True:
                bot.get_screenshot_as_file(f'screenshots/next_{i}.png')
              
              next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
              next_button.click()
          else:
            if debug is True:
              bot.get_screenshot_as_file(f'screenshots/next_{i}.png')
            
            next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
            next_button.click()
            time.sleep(random.randint(2, 3))

      #time.sleep(random.randint(5, 15))
      #change video to public 
      #bot.find_element(By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]').click()
      time.sleep(1)
      done_btn = bot.find_element(By.XPATH, '//*[@id="done-button"]')
      done_btn.click()
      ##time.sleep(random.randint(1, 5))
      bot.quit()

    def Arguments():
      parser = argparse.ArgumentParser(description='Process some integers.')

      parser.add_argument('-u', '--user', help='[required] this is usage user@gmail.com:password ')

      parser.add_argument('-f', '--file', help='[required] path to video e.g. /home/user/media/video.mp4')

      parser.add_argument('-r', '--remove', help='[optional] this will delete the video after an successful upload.')

      parser.add_argument('-d', '--debug', help='[optional] creates Screenshots for easier troubleshooting.(you can also check scraper.log)')

      return parser

    def main():
      # check arguments 
      print("Disclaimer : since this is not using the official API this might brake.")

      parser = YouTubeBot.Arguments()
      args = parser.parse_args()

      if args.user:
        userword = args.user

        logging = ScraperTools.Tools_Logger()
        logging.info("recieved username and password. splitting them now")

        email, password = userword.split(':', 1)
        
        logging.info("Successfully recieved username and password")
        print("Successfully recieved username and password")
      
      if args.file:
        path_to_video = args.file

      if args.debug:
        debug = True
        os.mkdir('screenshots')
      else:
        debug = False        

      YouTubeBot.uploadBot(path_to_video, debug)
      print("check youtube channel.")
        
      # delete video after upload
      if args.remove:
        print("deleting video now.")
        logging.info("deleting video now.")
        os.remove(path_to_video)

YouTubeBot.main()