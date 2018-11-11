import json
import datetime as d

# Classes
class Article:
    text = ''  # The entire text of the article to process
    date = ''  # Formatted as a string in UTC date format

articles = []

with open('../data/posts.json', encoding='utf8') as f:
    data = json.load(f)

for post in data:
    oldDate = post[0]
    dt = d.datetime.strptime(oldDate, '%B %d, %Y at %I:%M %p')
    print(dt)
    post[0] = str(dt)

with open('../data/posts-time-corrected.json', 'w', encoding='utf8') as f:
  json.dump(data, f, ensure_ascii=False)