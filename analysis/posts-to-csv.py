import json
import pandas

with open('../data/posts-time-corrected.json', encoding='utf8') as f:
    data = json.load(f)

df = pandas.DataFrame(data)
df.to_csv('../data/posts-csv.csv', encoding='utf-8', index=False)