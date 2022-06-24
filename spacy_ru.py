import spacy
import os
from glob import glob
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
nlp = spacy.load('ru_core_news_lg')

all_tegi = []
final_tegi = []
tmp = []

def load_data(path):
    X = glob(os.path.join(path, "*.md"))
    return X

def tag_deleter(file):
    f = open(file, encoding='utf-8').readlines()
    for l in range(len(f)-1, 0, -1):
        if "TEG FOUNDER:" in f[l]:
            for dl in range(len(f)-1, l-1, -1):
                f.pop(dl)
    with open(file, 'w', encoding='utf-8') as F:
        F.writelines(f)

def find_teg(doc):
    local_tegi = []
    with open(doc, 'r+', encoding='utf-8') as f:
        text = f.read()
    text = nlp(text)

    for ent in text.ents:
        # if ent.label_ == "PERSON":
        #     tag = #Здесь можно задавать условие создания тегов
        line = ""
        lst = ent.text
        lst = lst.split()
        for word in lst:
            if 'NOUN' in word.tag.POS:
                word = morph.parse(word)[0]
                word = word.inflect({'nomn'}.word)
                
        print(line)

        tag="".join(c for c in line if c.isalpha())
        tag = tag.upper()
        if tag not in local_tegi:
            local_tegi.append(tag)
            if tag in all_tegi and tag not in final_tegi:
                final_tegi.append(tag)
            if tag not in all_tegi:
                all_tegi.append(tag)                
    tmp.append(local_tegi)

def create_tag(doc, num):
    with open(doc, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write("TEG FOUNDER:")
        for teg in tmp[num]:
            if teg in final_tegi:
                f.write('\n')
                f.write(f"#{teg}")

path = 'data/AC2/Флоренция'
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1

# Все работает, но есть огромный кастыль в виде списка tmp
# Его стоит грамотно перебросить в all_tegi