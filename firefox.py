import random
import string
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Define URLs
BASE_URL = "https://web.whatsapp.com/"

# Create the Firefox profile
firefox_profile_path = r"C:\Users\chris\AppData\Roaming\Mozilla\Firefox\Profiles\umcx07k5.WhatBot"  # Replace this with the path of your custom profile

# Create the Firefox browser instance.
firefox_options = FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument(f"--profile={firefox_profile_path}")
firefox_options.add_argument("--private-window")

# Specify the path to the GeckoDriver executable
gecko_driver_path = "path/to/geckodriver"

browser = webdriver.Firefox(executable_path=gecko_driver_path, options=firefox_options)

browser.get(BASE_URL)
browser.maximize_window()

# Wait for the conversation header element to be present using WebDriverWait
conversation_header_element = WebDriverWait(browser, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='conversation-header']"))
)

# Extract the phone number from the conversation header element
phone = conversation_header_element.text

print(f"Phone number: {phone}")

# Construct the CHAT_URL dynamically using the extracted phone number
CHAT_URL = f"https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

browser.get(CHAT_URL)
time.sleep(3)

# Your message here
message = 'CUM GANG'

while True:
    try:
        # Wait for the chat input box to be present and visible before sending the message
        input_box = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[
