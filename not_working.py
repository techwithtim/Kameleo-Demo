from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def click_element(driver, by, selector):
    element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((by, selector))
        )

    if element:
        element.click()

def find_element(driver, by, selector):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, selector))
    )
    return element

def google_sign_in(driver):
    time.sleep(2)

    # google sign in
    click_element(driver, By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div[2]/div[2]')

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    email = find_element(driver, By.XPATH, '//*[@id="identifierId"]')
    email.send_keys(os.getenv('EMAIL'))

    # next button
    click_element(driver, By.XPATH, '//*[@id="identifierNext"]/div/button')

    pwd = find_element(driver, By.NAME, 'password')
    time.sleep(1)
    pwd.send_keys(os.getenv('PASSWORD'))

    # next button
    click_element(driver, By.XPATH, '//*[@id="passwordNext"]/div/button')

def find_product(product_name):
    search = find_element(driver, By.CLASS_NAME, 'search-key')
    search.send_keys(product_name)

    click_element(driver, By.CLASS_NAME, "search-button")
    time.sleep(5)


driver.get('https://www.aliexpress.com/')

# close popup
click_element(driver, By.CLASS_NAME,"btn-close")

account = find_element(driver, By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div[5]/div[3]/span/a')
ActionChains(driver).move_to_element(account).perform()

# click join button
click_element(driver, By.CLASS_NAME, 'join-btn')

google_sign_in(driver)
time.sleep(12)
find_product('rtx 3060')
