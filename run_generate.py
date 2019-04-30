# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:23:20 2019

@author: jchar
"""

import torch
import nltk
import random


import helpers
import model
import generate

def clean_title(ptfile, textfile):
    nltk.download('stopwords')   #get stopwords (in, a, the, is, etc.)
    from nltk.corpus import stopwords
    en_stops = set(stopwords.words('english'))

    random_line=random.choice(list(open(textfile, encoding="utf8")))  
    first_word=random_line.split(' ', 1)[0]  #choose a random first word of a title in the given text file
    
    pt=torch.load(ptfile) #load/process pt model file
    x=generate.generate(pt, first_word) #priming string is randomized first word in text
    x=x.replace('\n', ' ') #remove new lines
    title_list=x.split(' ', -1) #last word of title is frequently cut off, so always remove last word
    title_list.pop()
    b2string=" "
    y=b2string.join(title_list)
    if title_list[-1] in en_stops: #if second to last word is a stopword, remove that one too
        title_list.pop()
        y=b2string.join(title_list)
    return(y)
