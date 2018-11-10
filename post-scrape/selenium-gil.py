import selenium
from selenium import webdriver
import json

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--mute-audio')
chromeOptions.add_argument('--log-level=3')
chromeOptions.add_argument('--silent')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chromeOptions)
driver.implicitly_wait(0)

driver.get('https://realtalk-princeton.tumblr.com/page/2700')

posts = []

while True:
    dates = driver.find_elements_by_class_name('post-date')
    questions = driver.find_elements_by_class_name('question-box')
    answers = driver.find_elements_by_class_name('post-content')

    for a in range(0, len(questions)):
        date = dates[a].get_attribute('innerText')
        question = questions[a].get_attribute('innerText')
        answer = answers[a].get_attribute('innerText')
        print(date)
        print(question)
        print(answer)
        posts.append([date, question, answer])

    next = driver.find_elements_by_id('next')
    if len(next) == 0:
        break
    next[0].click()

driver.close()

# dump posts as json
with open('posts.json', 'w', encoding='utf8') as outfile:
    json.dump(posts, outfile, ensure_ascii=False)
