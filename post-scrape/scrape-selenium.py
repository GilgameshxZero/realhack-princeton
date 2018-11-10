import selenium
from selenium import webdriver
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--mute-audio')
chromeOptions.add_argument('--log-level=3')
chromeOptions.add_argument('--silent')
driver = webdriver.Chrome('chromedriver.exe'), chrome_options=chromeOptions)
driver.implicitly_wait(0)

driver.get('http://www.japochi.com/?g=japochi#')

# scraping code here

driver.close()