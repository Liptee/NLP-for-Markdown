import spacy
import pymorphy2
from conf import *
from funcs import load_data
from funcs import tag_deleter_ru

morph = pymorphy2.MorphAnalyzer()
nlp = spacy.load('ru_core_news_lg')

all_tegi = []
final_tegi = []
tmp = []

def find_teg(doc):
    local_tegi = []
    with open(doc, 'r+', encoding='utf-8') as f:
        text = f.read()
    text = nlp(text)

    for ent in text.ents:
        if ent.label_ in positive_labels or ent.label_ in neutral_labels:
            tag="".join(c for c in ent.text if c.isalpha())
            tag = tag.upper()
            if tag not in local_tegi:
                local_tegi.append(tag)
                if tag in all_tegi and tag not in final_tegi:
                    final_tegi.append(tag)
                if tag not in all_tegi:
                    all_tegi.append(tag)                
    tmp.append(local_tegi)
    print(f"local_tegi:{len(local_tegi)}")
    print(f"all_tegi:{len(all_tegi)}")
    print(f"final_tegi:{len(final_tegi)}")
    print(f"tmp:{len(tmp)}")
    print()

def create_tag(doc, num):
    with open(doc, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write("TEG FOUNDER:")
        for teg in tmp[num]:
            if teg in final_tegi:
                f.write('\n')
                f.write(f"#{teg}")

path = "data/ru/AC2\Флоренция"
for doc in load_data(path):
    print(doc)
    tag_deleter_ru(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1