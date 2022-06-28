import os
from glob import glob

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

def tag_deleter_ru(file):
    f = open(file, encoding='utf-8').readlines()
    for l in range(len(f)-1, 0, -1):
        if "TEG FOUNDER:" in f[l]:
            for dl in range(len(f)-1, l-1, -1):
                f.pop(dl)
    with open(file, 'w', encoding='utf-8') as F:
        F.writelines(f)