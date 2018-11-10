
# from google.cloud import storage, language, bigquery
from google.cloud import language
import json

# extract data from json file
with open('posts-small.json') as f:
    data = json.load(f)
print("Extracted data from json file!")

# Set up our GCS, NL, and BigQuery clients
#storage_client = storage.Client()
nl_client = language.LanguageServiceClient()

#bq_client = bigquery.Client(project='real-talk-222106')

'''
dataset_ref = bq_client.dataset('news_classification_dataset')
dataset = bigquery.Dataset(dataset_ref)
table_ref = dataset.table('article_data')
table = bq_client.get_table(table_ref)
'''


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


# rows_for_bq = []
#nl_response = classify_text("I hate this place and its exam curves. At least for me, it's a no-win situation. if an exam is really hard, I tank it and get a bad grade. If it's really easy, the curve shoots up and I still get a bad grade.".encode("utf8").decode("utf8"))
#print(nl_response)


# Send files to the NL API and save the result to send to BigQuery
for file in data:
    
    dtime = file[0]
    question = file[1]
    answer = file[2]
    print(dtime)
    print(question)
    try:
    	nl_response = classify_text(question)
    	print(nl_response)
    except:
    	pass

                #if len(nl_response.categories) > 0:
                   #     rows_for_bq.append((article_text, nl_response.categories[0].name, nl_response.categories[0].confidence))


'''
#print("Writing NL API article data to BigQuery...")
# Write article text + category data to BQ
#errors = bq_client.create_rows(table, rows_for_bq)
#assert errors == []
'''

