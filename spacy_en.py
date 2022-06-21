import spacy
import os
from glob import glob

nlp = spacy_new.load('en_core_web_sm')

all_tegi = []
final_tegi = []
def load_data(path):
    X = glob(os.path.join(path, "*.md"))
    return X

def tag_deleter(file):
    f = open(file).readlines()
    for l in range(len(f)-1, 0, -1):
        if "TEG FOUNDER:" in f[l]:
            for dl in range(len(f)-1, l-1, -1):
                f.pop(dl)
    with open(file, 'w') as F:
        F.writelines(f)

def find_teg(doc):
    with open(doc, 'r+') as f:
        text = f.read()

    tegi = []
    tmp = nlp(text)
    for ent in tmp.ents:
        tag="".join(c for c in ent.text if c.isalpha())
        if tag not in tegi:
            tegi.append(tag)
        if tag in tegi and tag not in final_tegi:
            final_tegi.append(tag)

def create_teg(doc):
    with open(doc, 'r+') as f:
        text = f.read()

    tegi = []
    tmp = nlp(text)
    for ent in tmp.ents:
        tag="".join(c for c in ent.text if c.isalpha())
        if tag not in tegi and tag in final_tegi:
            tegi.append(tag)

    with open(doc, 'a') as f:
        f.write('\n')
        f.write("TEG FOUNDER:")
        for teg in tegi:
            f.write('\n')
            f.write(f"#{teg}")

path = "data/en_data"
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)
for doc in load_data(path):
    create_teg(doc)
