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
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    en_stops = set(stopwords.words('english'))

    random_line=random.choice(list(open(textfile, encoding="utf8")))
    first_word=random_line.split(' ', 1)[0]
    
    pt=torch.load(ptfile)
    x=generate.generate(pt, first_word)
    x=x.replace('\n', ' ')
    title_list=x.split(' ', -1)
    title_list.pop()
    b2string=" "
    y=b2string.join(title_list)
    if title_list[-1] in en_stops:
        title_list.pop()
        y=b2string.join(title_list)
    return(y)

clean_title("all_titles.pt", "all_titles.txt")
   