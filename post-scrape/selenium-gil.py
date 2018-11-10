import selenium
from selenium import webdriver
import json
import os
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--mute-audio')
chromeOptions.add_argument('--log-level=3')
chromeOptions.add_argument('--silent')

#lines 16 and 17 are only necessary for Mac OS
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN =os.path.join(PROJECT_ROOT,"chromedriver")
driver = webdriver.Chrome(DRIVER_BIN, chrome_options=chromeOptions)
driver.implicitly_wait(0)

driver.get('https://realtalk-princeton.tumblr.com/page/1')

posts = []

while True:
    dates = driver.find_elements_by_class_name('post-date')
    questions = driver.find_elements_by_class_name('question-box')
    answers = driver.find_elements_by_class_name('post-content')
    # finds elements returns arrays

    for a in range(0, len(questions)):
        date = dates[a].get_attribute('innerText')
        question = questions[a].get_attribute('innerText')
        answer = answers[a].get_attribute('innerText')
        print(date)
        print(question)
        print(answer)
        posts.append([date, question, answer])
    break

    next = driver.find_elements_by_id('next') #id of the next button is next
    if len(next) == 0:
        break
    next[0].click() #array 0 because next is an array

# dump posts as json
with open('posts.json', 'w', encoding='utf8') as outfile:
    json.dump(posts, outfile, ensure_ascii=False)

driver.close()
