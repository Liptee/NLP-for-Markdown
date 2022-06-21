from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk import ne_chunk_sents
from nltk import pos_tag
import nltk
import numpy as np
import os
from glob import glob

def load_data(path):
    X = glob(os.path.join(path, "*.md"))
    return X

def create_tag(doc):
    with open(doc, 'r+') as f:
        full = f.read()
    
    sents = sent_tokenize(full)
    token_sents = [word_tokenize(sent) for sent in sents]
    tagged_sents = [pos_tag(sent) for sent in token_sents]
    chunked_sents = ne_chunk_sents(tagged_sents)
    tags = []
    for tree in chunked_sents:
        for word in tree:
            if 'nltk' in str(type(word)) and list(word) not in tags:
                tags.append(list(word))
    
    tegi = []
    for tag in tags:
        if len(tag) == 1:
            tegi.append(tag[0][0].upper())
        else:
            string = tag[0][0]
            for ex in tag[1:]:
                string+="_"
                string+=ex[0]
            tegi.append(string.upper())

    with open(doc, 'a') as f:
        f.write('\n')
        f.write("TEG FOUNDER:")
        for teg in tegi:
            f.write('\n')
            f.write(f"#{teg}")
        tag_deleter(doc)

def tag_deleter(file):
    f = open(file).readlines()
    for l in range(len(f)-1, 0, -1):
        if "TEG FOUNDER:" in f[l]:
            for dl in range(len(f)-1, l-1, -1):
                f.pop(dl)
    with open(file, 'w') as F:
        F.writelines(f)


path = "dataz"
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    create_tag(doc)