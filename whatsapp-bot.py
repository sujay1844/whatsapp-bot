#!/usr/bin/env python

# This is a script to automate Whatsapp messaging
# For now, it supports only Firefox

contact = ""
msg = ""
profile_path = ""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    # Importing variable from .env
    from dotenv import load_dotenv
    import os
    load_dotenv()
    contact = os.getenv("CONTACT")
    msg = os.getenv("MESSAGE")
    profile_path = os.getenv("PROFILE_PATH")
except Exception as err:
    if profile_path == "" or contact == "" or msg == "":
        print("Change contact, msg and profile_path variables at the beginning of this script")
        exit()

# If you don't want to use your default profile, you need to scan QR code every time
opts = webdriver.FirefoxOptions()
opts.add_argument("--profile " + profile_path)
browser = webdriver.Firefox(options=opts)

# Navigate to Whatsapp Web
browser.get("https://web.whatsapp.com")

# Search for the contact
search_xpath = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]"
# The script would complain that element not found
# It won't be found because it is not loaded yet
# The following line waits for the page to load
search_box = WebDriverWait(browser, 50).until(lambda browser:
                                                  browser.find_element(By.XPATH, search_xpath))
search_box.click()
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)

# Type in the message and press enter
msg_box_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]"
msg_box = WebDriverWait(browser, 50).until(lambda browser:
                                                   browser.find_element(By.XPATH, msg_box_xpath))
msg_box.click()
for x in msg:
    msg_box.send_keys(x)
input("Press enter to send message...")
msg_box.send_keys(Keys.ENTER)

input("Press enter to quit...")
browser.close()
