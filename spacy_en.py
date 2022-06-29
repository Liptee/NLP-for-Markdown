import spacy
from itertools import chain
from conf import *
from funcs import (
    load_data,
    tag_deleter
)

nlp = spacy.load("en_core_web_sm")

all_tegi = []
final_tegi = []

def find_teg(doc):
    local = []
    with open(doc, 'r+', encoding="utf-8") as f:
        text = f.read()
    text = nlp(text)

    for ent in text.ents:
        if ent.label_ in positive_labels:
            tag = ent.text
            tag = tag.replace(" ", "_")
            for ch in char_set:
                tag = tag.replace(ch, "")
            tag = tag.upper()

            if tag not in local:
                local.append(tag)
                if tag in list(chain(*all_tegi)) and tag not in final_tegi:
                    final_tegi.append(tag)
    all_tegi.append(local)
    print(f"local_tegi:{len(local)}")
    print(f"all_tegi:{len(all_tegi)}")
    print(f"final_tegi:{len(final_tegi)}")
    print()

def create_tag(doc, num):
    with open(doc, 'a', encoding="utf-8") as f:
        first = True
        for teg in all_tegi[num]:
            if teg in final_tegi:
                if first:
                    f.write('\n')
                    f.write("TEG FOUNDER:")
                    first = False
                f.write('\n')
                f.write(f"#{teg}")

path = "data/en/en_data_spacy"

for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1