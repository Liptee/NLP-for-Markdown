from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk import ne_chunk_sents
from nltk import pos_tag

from funcs import load_data
from funcs import tag_deleter
from itertools import chain

all_tegi = []
final_tegi = []

def find_teg(doc):
    local = []
    with open(doc, 'r+', encoding='utf-8') as f:
        text = f.read()

    sents = sent_tokenize(text)
    token_sents = [word_tokenize(sent) for sent in sents]
    tagged_sents = [pos_tag(sent) for sent in token_sents]
    chunked_sents = ne_chunk_sents(tagged_sents)

    for tree in chunked_sents:
        for word in tree:
            if "nltk" in str(type(word)):
                if len(list(word)) == 1:
                    teg = list(word)[0][0]

                else:
                    teg = ""
                    for w in list(word):
                        teg+=f"{str(w[0])}_"
                    teg = teg[:-1]
                    teg = teg.upper()              
                if teg not in local:
                    local.append(teg)
                    if teg in list(chain(*all_tegi)) and teg not in final_tegi:
                        final_tegi.append(teg)
    all_tegi.append(local)

    print(f"local_tegi:{len(local)}")
    print(f"all_tegi:{len(all_tegi)}")
    print(f"final_tegi:{len(final_tegi)}")
    print()

def create_tag(doc, num):
    with open(doc, 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write("TEG FOUNDER:")
        for teg in all_tegi[num]:
            if teg in final_tegi:
                f.write('\n')
                f.write(f"#{teg}")

path = 'data/en/en_data_nltk'
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1