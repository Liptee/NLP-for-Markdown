from itertools import chain
import natasha
from funcs import(
    tag_deleter,
    load_data
)
from natasha import (
    Doc,
    NewsNERTagger,
    NewsEmbedding,
    Segmenter,
    MorphVocab,
    NewsMorphTagger
)

emb = NewsEmbedding()
segmenter = Segmenter()
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()
morph_tagger = NewsMorphTagger(emb)

all_tegi = []
final_tegi = []

def find_teg(doc):
    local = []
    with open(doc, "r+", encoding='utf-8') as f:
        text = f.read()

    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)
        tag = span.normal
        tag = tag.replace(" ", "_")
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

path = "data/ru/AC2\Флоренция"
for doc in load_data(path):
    print(doc)
    tag_deleter(doc)
    find_teg(doc)

count = 0
for doc in load_data(path):
    create_tag(doc, count)
    count+=1