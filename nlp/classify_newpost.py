#!/usr/bin/python
from google.cloud import language
import json
import sys

# extract data from json file
'''with open('posts-small.json') as f:
    data = json.load(f)
print("Extracted data from json file!") '''

nl_client = language.LanguageServiceClient()

# Send article text to the NL API's classifyText method
def classify_text(article):
    print(article)
    print("length: ")
    print(len(article))
    nl_client = language.LanguageServiceClient()

    document = language.types.Document(
            content=article, type=language.enums.Document.Type.PLAIN_TEXT)

    response = nl_client.classify_text(document)

    print(response.categories)
    return response


# Store question as the string passed in the argument
question = str(sys.argv)
    
#dtime = file[0]
#question = file[1]
#answer = file[2]
print(question)
try:
	nl_response = classify_text(question)
	print(nl_response)
except:
    pass



