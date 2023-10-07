#sends the message "CUM GANG" to the designated user every 20 seconds
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#Phone number must be appended with international code without plus sign. 
#read phone number from config file
with open("private/config.txt", "r+") as file:
    # Read the first line
    phone = file.readline().strip()
#if the file is empty, get the number from the user and write it to the file
    if phone=='':
        file.seek(0)  # Move the file pointer to the beginning
        file.write(phone)
        file.truncate()  # Remove any extra characters if the new phone number is shorter than the previous one

message = 'CUM GANG'

#Define Urls
BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"


# Create the chrome browser instance.
chrome_options = Options()
chrome_options.add_argument("start-maximized")
user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=chrome_options,
)

browser.get(BASE_URL)
browser.maximize_window()


browser.get(CHAT_URL.format(phone=phone))
time.sleep(3)

while True:
    #Now search the chat input box using XPath and enter the message. Send the ENTER key after it.
    inp_xpath = (
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    )
    input_box = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
    )
    try:
        # Wait for the elements with the "message-out" class to be present using WebDriverWait
        message_out_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".message-out"))
        )

        # Iterate through the elements and print their text (messages)
        for element in message_out_elements:
            print(element.text)
    except TimeoutException:
        # Handle the TimeoutException here.
        print("Timed out while waiting for the elements. Retrying...")


    input_box.send_keys(message)
    #input_box.send_keys(Keys.CONTROL+"v")
    #input_box.send_keys(Keys.ENTER)
    input_box.send_keys(Keys.ENTER)
    time.sleep(20)
    
time.sleep(5)