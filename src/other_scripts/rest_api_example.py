"""
API Documentation: https://www.datamuse.com/api/

REST API Function to get 5 Rhyming words for a given word
"""

import requests


def getRhymingWords(stringx):
    base_url = "https://api.datamuse.com/words" # /words endpoint, in Datamuse API URL
    api_params = {"rel_rhy":stringx, "max":1}   # Parameters for the /words endpoint

    muse_page = requests.get(base_url, params=api_params)   # API Call

    # print(type(muse_page), "\n", muse_page) # Type of the object, Response Object
    muse_page_json = muse_page.json() # Convert JSON to Python Datastructure (Either list or Dict)
    # print(type(muse_page_json), "\n",muse_page_json)  # Type of Object returned

    rhyme_words = [rhy_dict['word'] for rhy_dict in muse_page_json] # Extracting data from list of dictionaries 

    # print(rhyme_words)
    return rhyme_words

def alternateSentence(stringx):
    alternate_stringx = ""
    words_list = stringx.split()

    list_obtained = []
    for index, word in enumerate(words_list):
        list_obtained.append(getRhymingWords(word))
        alternate_stringx = alternate_stringx + list_obtained[index][0] + " "

    return (list_obtained, alternate_stringx)


print(alternateSentence("Get out of the Car"))    