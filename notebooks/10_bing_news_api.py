import json
import os
import requests
import time
from datetime import datetime



'''
This sample makes a call to the Bing News Search API with a text query and returns relevant news webpages.
Documentation: https: // docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/
'''


# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscriptionKey = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
endpoint = "https://api.bing.microsoft.com/v7.0/news"


# Construct a request
query = ""
categories = ["World", "Business", "Sports", "Science"]
count = 100
freshness = "Day"
mkt = 'en-US'
data_file_path = os.path.abspath(os.path.join(os.pardir,'data','bing_api_json'))


for category in categories:
    params = {'q': query, 'mkt': mkt, 'category': category, 'count': count, 'freshness': freshness}
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    file_name = datetime.today().strftime('%Y%m%d') + "_" + category

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        #write json string to file
        with open(data_file_path+file_name+'.json', 'w') as json_file:
          json.dump(response.json(), json_file)
    except Exception as ex:
        raise ex

    time.sleep(1)
    #free account offers only 3 requests per second




#9 requests as of 3/21/21
