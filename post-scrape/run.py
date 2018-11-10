import requests
r = requests.get(
    'https://api.tumblr.com/v2/blog/realtalk-princeton/posts/text?api_key=Sa9QsJ9MzOOoDBOHEwWLuLyFD4Bz1mCEQCxLQz3kbbBCiOjoza')
print(r.status_code)
print(r.text)
