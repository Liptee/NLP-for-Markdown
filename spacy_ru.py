from spacy.lang.ru import Russian

nlp = Russian()
doc = "data/AC2/Венеция/Венеция.md"
with open(doc, 'r+', encoding='utf-8') as f:
    full = f.read()

doc = nlp(full)
#is_alpha проверка на полнобуквенные токены
print("is_alpha: ", [token.is_alpha for token in doc])
print()
#is_punct проверка на знак пунктуации 
print("is_punct:    ", [token.is_punct for token in doc])
print()
#like_num проверка на число
print("like_num:    ", [token.like_num for token in doc])

#СК выводит токены перед точкой
for token in doc:
    if token.i+1 < len(doc):
        next_token = doc[token.i+1]
        if next_token.text == ".":
            print(token.text)