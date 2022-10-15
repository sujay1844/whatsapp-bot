#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

contact = "Skandan Schl"
msg = "This message was sent by a bot"

profile_path = "/home/sujay1844/.mozilla/firefox/y4gt43vs.default-release"
opts = webdriver.FirefoxOptions()
opts.add_argument("--profile "+ profile_path)
browser = webdriver.Firefox(options=opts)

browser.get("https://web.whatsapp.com")

# input("Scan QR Code and press enter...")
# print("Logged in (hopefully)...")

search_box_xpath = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]"
search_box = WebDriverWait(browser, 50).until(lambda browser:
                                browser.find_element(By.XPATH, search_box_xpath))

search_box.click()
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)

# Type in the message and press enter
message_box_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]"
message_box = WebDriverWait(browser, 50).until(lambda browser:
                                browser.find_element(By.XPATH, message_box_xpath))
message_box.click()
for x in msg:
    message_box.send_keys(x)
input("Press enter to send message...")
message_box.send_keys(Keys.ENTER)


input("Press enter to quit")
browser.close()
