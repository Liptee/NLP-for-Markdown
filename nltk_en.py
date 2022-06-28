from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from nltk import ne_chunk_sents
from nltk import pos_tag

from funcs import load_data
from funcs import tag_deleter

all_tegi = []
final_tegi = []
tmp = []

def find_teg(doc):
    local_tegi = []
    with open(doc, 'r+') as f:
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
                    if teg not in local_tegi:
                        local_tegi.append(teg)                
                if teg not in final_tegi and teg not in local_tegi and teg in all_tegi:
                    final_tegi.append(teg)
                if teg not in local_tegi:
                    local_tegi.append(teg)
                    if teg not in all_tegi:
                        all_tegi.append(teg)
    
    tmp.append(local_tegi)
    print(f"local_tegi:{len(local_tegi)}")
    print(f"all_tegi:{len(all_tegi)}")
    print(f"final_tegi:{len(final_tegi)}")
    print(f"tmp:{len(tmp)}")
    print()

def create_tag(doc, num):
    with open(doc, 'a') as f:
        f.write('\n')
        f.write("TEG FOUNDER:")
        for teg in tmp[num]:
            if teg in final_tegi:
                f.write('\n')
                f.write(f"#{teg}")


all_tegi = []
final_tegi = []
tmp = []

path = 'data/en/en_data_nltk'
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1