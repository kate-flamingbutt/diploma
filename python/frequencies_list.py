# coding=utf8
dir='C:\\Users\\ekaterina.morozova\\Desktop\\corpus_tst'
from pymystem3 import Mystem
import re
import collections
m = Mystem()
def lemmatize_sentence(text):
    lemmas = m.lemmatize(text)
    return list(filter(None,re.split(r'[^а-яА-Я-]+',"".join(lemmas).strip())))
def get_words_freq(fname):
    f = open(fname, 'r', encoding='utf-8')
    txt=f.read()
    l=collections.Counter(lemmatize_sentence(txt))
    f.close()
    return l
import os
for f in os.listdir(dir):
    print(f)
    print(get_words_freq(os.path.join(dir, f)))
    print('\n\n')