import copy
import pickle

import pandas as pd
import numpy as np
import sys
import re
from sklearn.utils import shuffle

from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
import random
pd.set_option("display.max_rows", 1000)    #display max. 1000 rows
pd.set_option("display.max_columns", 1000) #display max. 1000 columns

import os

from sklearn.model_selection import train_test_split

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

"""
@author: Hsin Yi Chiu
@version: 2020-04-09
the code is refer from kaggle "Searching the million news with TF-IDF" : 
https://www.kaggle.com/chechir/searching-the-million-news-with-tf-idf
"""


def preprocess_for_query(sentence):
    """
    clear the query sentence to find the base form of the word like in the dictionary
    :param sentence: the query from user
    :return: a sentence only with the base form of the word
    """
    sentence= re.sub(r'([^\s\w]|\\_)+','',sentence)

    stemmer = SnowballStemmer('english')
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w in stopwords.words('english')]
    words= ' '.join(stemmer.stem(w) for w in filtered_sentence)

    return words

def get_cosine(sentence):
    """
    get the cosine similarity of the query and product
    :param sentence: the query from the user that has been preprocessed
    :return: the cosine score of the query and product
    """

    vectoriser= pickle.load(open('../temp/vect','rb'))
    fit_transform= pickle.load(open('../temp/tfidf','rb'))
    fitted_tfidf= pickle.load(open('../temp/fitted_tfidf','rb'))

    query_vectorised= vectoriser.transform([sentence])
    query_tfidf= fit_transform.transform(query_vectorised)
    cosine_similarities = linear_kernel(fitted_tfidf, query_tfidf).flatten()
    return cosine_similarities

def get_search(sentence,max_rows=3):
    """
    seach engine to recommend the most similar product based on what user searchs
    :param sentence: the query from user
    :param max_rows: top 3 closed scores
    :return: the closet product
    """
    #df= pd.read_csv('/content/gdrive/My Drive/file/word_bag.csv')
    df= pd.read_csv('../product.csv')
    df=df.fillna('nan')

    score = get_cosine(preprocess_for_query(sentence))
    results_df = copy.deepcopy(df)
    results_df['ranking_score'] = score
    print(results_df['ranking_score'].head(3))
    results_df = results_df.loc[score>0]
    results_df = results_df.iloc[np.argsort(-results_df['ranking_score'].values)]
    results_df = results_df.head(max_rows)

    return_result=[]
    for index, row in results_df.iterrows():
        results_temp=[]
        asin= row['asin']
        brand = row['brand']
        title= row['title']
        results_temp.append(asin)
        results_temp.append(brand)
        results_temp.append(title)
        return_result.append(results_temp)

    return return_result

#output= get_search('I need to find a colorful skirt for a wedding')
#print(type(get_cosine('I need to find a colorful skirt for a wedding')))
#for i in output:
 #   print(i)


"""
df= pd.read_csv('../x11/x11_word_bag.csv')
print(df.head(3))


test= pd.read_csv('../x11/y11.cs')
print(len(test))

test= shuffle(test)
test= test.drop_duplicates()
print(len(test))

test= test.sample(n=100)
print(len(test))

x= len(test)
correct=0
not_match=0
n=1
dict_temp={}
for index, row in test.iterrows():
    asin= row['asin']

    text= row['sentence']

    back_result= get_search(text)
    if back_result== asin:
        correct+=1
    else:
        not_match+=1
    percentage= correct/n*100
    remain= x-n
    dict_temp= {'index':index,'y_asin':asin,'return_result':back_result,'correct':correct,'not_macth':not_match,'correct_per':percentage}
    print(remain,correct,not_match,percentage,index,asin,back_result)
    n+=1


percentage= correct/n*100
print(n,correct,not_match)

file= pd.DataFrame.from_dict(dict_temp)
file.to_csv('../x11/result.csv',index=False)
print('file done')"""