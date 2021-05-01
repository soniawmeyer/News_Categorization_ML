#this program takes several json files from the bing news api
#collected via bing_new_api.py and converts them to one concatenated dataframe
#of only the category, title, and description, then removes stopwords and punctuation
#and lemmatizes what remains
#this gives us only the most important keyword on which to categorize the news article

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import string
from num2word import word
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import WordNetLemmatizer
import os

data_file_path = os.path.abspath(os.path.join(os.pardir,'data','bing_api_json',''))
mac = '/'
# windows = '\\'

#dict of json files from bing news api
dict = {'sports':['20210321_Sports.json','20210410_Sports.json','20210429_Sports.json'],
        'world':['20210321_World.json','20210410_World.json','20210429_World.json'],
        'business':['20210321_Business.json','20210410_Business.json','20210429_Business.json'],
        'science_and_technology':['20210321_Science.json','20210410_Science.json','20210429_Science.json']}

df_list = []

#iterates through each json file and stores as a dataframe in a list
for k, v in dict.items():
    for i in v:
        init_df = pd.read_json(data_file_path+mac+i)
        df = json_normalize(init_df['value'])
        df = df[['name','description']]
        df.insert(0, 'News Category', k)
        df_list.append(df)
        df.head()

#concatenates list of dataframes into one dataframe
data = pd.concat(df_list,axis=0)
#renames column title to match other data
data = data.rename(columns={'name':'Title', 'description': 'Description'})
data.shape
data.head()

#Below is Fengling's code unedited except adding comments
#Remove Punctuation and Stopwords
print(STOPWORDS)
print(string.punctuation)
data['Title'] = data['Title'].str.translate(str.maketrans('','',string.punctuation)).str.lower()
data['Description'] = data['Description'].str.translate(str.maketrans('','',string.punctuation)).str.lower()


def convert_num_to_word(words):
    result = []
    for w in words:
        if w.isnumeric():
            result.extend(map(lambda x: x.lower(),word(w).split()))
        else:
            result.append(w)
    return result

data['Title'] = data['Title'].str.split().apply(convert_num_to_word)
data['Description'] = data['Description'].str.split().apply(convert_num_to_word)


def remove_stopword(words):
    result = []
    for word in words:
        if word not in STOPWORDS:
            result.append(word)
    return result

data['Title'] = data['Title'].apply(remove_stopword)
data['Description'] = data['Description'].apply(remove_stopword)


def remove_single_character(words):
    result = []
    for word in words:
        if len(word) > 1:
            result.append(word)
    return result

data['Title'] = data['Title'].apply(remove_single_character)
data['Description'] = data['Description'].apply(remove_single_character)



#Lemmatization
#this groups words based on their lemma ex: walk v walked v walking

def lemmatization(words):
    lemmatizer = WordNetLemmatizer()
    result = []
    for word in words:
        result.append(lemmatizer.lemmatize(word))
    return result

data['Title'] = data['Title'].apply(lemmatization)
data['Description'] = data['Description'].apply(lemmatization)

data.head()


#export to csv
export_file_path = os.path.abspath(os.path.join(os.pardir,'data','real_time_data_processed.csv'))
data.to_csv(export_file_path)
