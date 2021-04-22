#!/usr/bin/env python3

import os
import subprocess
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def create_profile(profile_dir):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={profile_dir}')
    with webdriver.Chrome(options=options) as driver:
        driver.get('https://web.whatsapp.com')
        input('Link Browser with QR Code, then press Enter ')
        print(f'Profile saved to {profile_dir}')

def run(profile_dir):
    with subprocess.Popen('Xvfb :42'.split()) as proc:
        os.environ['DISPLAY'] = ':42'
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-data-dir={profile_dir}')
        with webdriver.Chrome(options=options) as driver:
            driver.get('https://web.whatsapp.com')
            while True:
                try:
                    # regularly "click" on the chat search bar to stay "active"
                    search_bar = driver.find_element_by_class_name('RPX_m')
                    search_bar.click()
                except NoSuchElementException:
                    pass
                time.sleep(3)

if __name__ == '__main__':
    command = sys.argv[1]
    profile_dir = sys.argv[2]
    if command == 'create_profile':
        create_profile(profile_dir)
    elif command == 'run':
        run(profile_dir)
