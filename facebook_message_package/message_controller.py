import random

from flask import Flask, request
from fbmq import Page,Attachment,Template,QuickReply

from gensim.parsing import preprocess_string
import content_based_package.recommend_matched_item as s
import content_based_package.search_engine as e



#popularity item of each tags
def occasion_answer(tags):
    """
    this method is to provide the matched item for users based on the selection that they select
    the program would provide the prediction
    :param tags: the occasion selection from user
    :return: top 5 recommended product
    """
    for_man= ['top','jeans','bottom','hoodies','coats','jackets','sweaters',
              'jumper','cardigan','vest','t-shirt','trainer','sandal','loafer','sunglasses','tie','boots','jewellery',
              'socks','belt','watches','bags']
    for_woman=['top','jeans','bottom','hoodies','coats','jackets','sweaters',
               'jumper','cardigan','vest','t-shirt','trainer','sandal','loafer','sunglasses','tie','dress','skirt','necklace',
               'boots','earring','bags']
    product=''
    if tags=='Party for man':

        items=random.choices(for_man,k=int(random.randrange(len(for_man))))
        search_item= ' '.join(word[0] for word in items)+' '+'party man'
        tags='man,female,woman'
        product= s.search(search_item,tags)

    elif tags=='Wedding for man':
        items=random.choices(for_man,k=int(random.randrange(len(for_man))))
        search_item= ' '.join(word[0] for word in items)+' '+'wedding man'
        tags='man,female,woman'
        product= s.search(search_item,tags)


    elif tags=='Outdoor for man':
        items=random.choices(for_man,k=int(random.randrange(len(for_man))))
        search_item= ' '.join(word[0] for word in items)+' '+'outdoor man'
        tags='man,female,woman'
        product= s.search(search_item,tags)

    elif tags=='Work for man':
        items=random.choices(for_man,k=int(random.randrange(len(for_man))))
        print(items)
        search_item= ' '.join(word[0] for word in items)+' '+'work man'
        tags='man,female,woman'
        product= s.search(search_item,tags)

    elif tags=='Party for woman':
        items=random.choices(for_man,k=int(random.randrange(len(for_woman))))

        search_item= ' '.join(word[0] for word in items)+' '+'woman'
        tags='woman,male,man'
        product= s.search(search_item,tags)

    elif tags=='Wedding for woman':
        items=random.choices(for_man,k=int(random.randrange(len(for_woman))))
        search_item= ' '.join(word[0] for word in items)+' '+'wedding woman'
        tags='woman,male,man'
        product= s.search(search_item,tags)

    elif tags=='Outdoor for woman':
        items=random.choices(for_man,k=int(random.randrange(len(for_woman))))
        search_item= ' '.join(word[0] for word in items)+' '+'outdoor woman'
        tags='woman,male,man'
        product= s.search(search_item,tags)

    elif tags=='Work for woman':
        items=random.choices(for_man,k=int(random.randrange(len(for_woman))))
        search_item= ' '.join(word[0] for word in items)+' '+'work woman'
        tags='woman,male,man'
        product= s.search(search_item,tags)

    else:
        product=s.search(tags)

    return product

#specific item based on the request
def specific_answer(sentence):
    """
    this method is for the query search that user just typed their requirement into the box
    :param sentence: the query
    :return: the most similar product that from TFIDF result
    """
    product= e.get_search(sentence)
    return product

#print(occasion_answer("Work for man"))