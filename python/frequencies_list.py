# coding=utf8
dir='C:\\Users\\ekaterina.morozova\\Desktop\\deeplom\\diploma\\corpus'
#dir='C:\\Users\\ekaterina.morozova\\Desktop\\deeplom\\diploma\\tst'
from pymystem3 import Mystem
import re
import collections
def get_stop_words():
    f=open('C:\\Users\\ekaterina.morozova\\Desktop\\deeplom\\diploma\\stop_words.txt', 'r', encoding='utf-8')
    lines=f.read()
    return list(filter(None,re.split(r'\n',lines)))
m = Mystem()
def lemmatize_sentence(text):
    lemmas = m.lemmatize(text)
    return list(filter(None,re.split(r'[^а-яА-Я-]+',"".join(lemmas).strip())))
def minus_stop_words(word_list):
    stop_list=get_stop_words()
    res_list=[]
    for i in word_list:
        if i not in stop_list:
            res_list.append(i)
    return res_list
def minus_stop_words_txt(text):
    stop_list = get_stop_words()
    for i in stop_list:
        text=text.replace(' '+i,'')
    return text
import pytils
def transliter_file(fname):
    f = open(fname, 'r', encoding='utf-8')
    txt = f.read()
    txt_tr=pytils.translit.translify(txt)
    f_o=open(fname+'_trans', 'a')
    f_o.write(txt_tr)
    f_o.close()

def trans_lemm(fname, remove_stop_w_flg=0):
    f = open(fname, 'r', encoding='utf-8')
    txt = f.read()
    if (len(txt) > 50000):
        txt = txt[0:50000]
    lemm = m.lemmatize(txt)
    print(lemm)
    if (remove_stop_w_flg):
        lemm = minus_stop_words(lemm)
    lemm=[pytils.translit.translify(i) for i in lemm]
    f_o = open(fname + '_trans_lemm'+str(remove_stop_w_flg), 'a')
    for l in lemm:
        f_o.write(l)
    f_o.close()


def get_words_freq(fname, remove_stop_w_flg=0):
    f = open(fname, 'r', encoding='utf-8')
    txt=f.read()
    if (len(txt) > 50000):
        txt=txt[0:50000]
    lemm=lemmatize_sentence(txt)
    if(remove_stop_w_flg):
        lemm=minus_stop_words(lemm)
    l=collections.Counter(lemm)
    f.close()
    return { key:value for (key,value) in l.items() if value >= 5}
import os
f_o=open('C:\\Users\\ekaterina.morozova\\Desktop\\deeplom\\diploma\\corpus_freq_counter_stops.txt','a')
for f in os.listdir(dir):
    if (not f.endswith('.txt')):
        continue
    print(f)
    '''g = get_words_freq(os.path.join(dir, f))
    s_g=sorted( ((v,k) for k,v in g.items()), reverse=True)
    print(s_g)
    f_o.write(f+' first 50k syms: \n')
    for i in s_g:
        f_o.write(i[1]+': '+str(i[0])+'\n')
    print('\n')'''
    g = get_words_freq(os.path.join(dir, f),1)
    s_g = sorted(((v, k) for k, v in g.items()), reverse=True)
    print(s_g)
    f_o.write(f + ' first 50k syms w/o stopwords: \n')
    for i in s_g:
        f_o.write(i[1] + ': ' + str(i[0]) + '\n')
    print('\n\n')
    trans_lemm(os.path.join(dir, f),0)
    trans_lemm(os.path.join(dir, f),1)
f_o.close()