# -*- coding: utf8 -*-
long_dash = True
fir_like = True
fix_pars = True
add_tags = True
MODE = 'words'
LANG = 'ru'
pron_ru=["я", "ты", "мы", "вы", "все", "он", "она", "оно", "они", "себя", "мой", "твой", "наш", "ваш", "свой", "кто", "что", "какой", "каков", "который", "чей", "скольк", "никто", "ничто", "некого", "нечего", "никако", "ничей", "нисколько", "некто", "нечто", "некотор", "кто-то", "сколько-то", "что-либо", "кое-кто", "какой-то", "какой-либо", "кое-какой", "чей-то", "чей-нибудь", "сам", "кажд", "люб", "всяк", "цел", "ин", "весь", "другой", "это", "тот", "такой", "таков", "тот-то", "такой-то", "столько", "столько-то", "меня", "мне", "мной", "тебя", "тебе", "тобой", "нас", "нам", "нами", "вас", "вам", "вами", "его", "ему", "им", "ее", "ей", "нем", "ней", "него", "нее", "нему", "ним", "их", "них", "ими", "ними", "моего", "моему", "моем", "моим", "твоего", "твоему", "твоим", "твоем", "нашего", "нашему", "нашим", "нашем", "вашего", "вашему", "вашим", "вашем", "своего", "своему", "своим", "своем", "кого", "кому", "кем", "ком", "чего", "чему", "чем", "какого", "какому", "каким", "каком", "которого", "которому", "которым", "котором", "чьего", "чьему", "чьими", "чьем", "никому", "никем", "ничем", "никаким", "ничьим", "другого", "другому", "другим", "другом"]
pro_nouns = ['я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они', 'кто', 'что', 'некто', 'нечто', 'кое-кто', 'кое-что', 'кто-либо', 'кто-нибудь', 'никто', 'ничто', 'тот', 'каждый', 'сам', 'иной', 'другой']
proper_prons = ['я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они']
en_pro_nouns = ["all", "another", "any", "anybody", "anyone", "anything", "as", "aught", "both", "each", "each other", "either", "enough", "everybody", "everyone", "everything", "few", "he", "her", "hers", "herself", "him", "himself", "his", "I", "idem", "it", "its", "itself", "many", "me", "mine", "most", "my", "myself", "naught", "neither", "no one", "nobody", "none", "nothing", "nought", "one", "one another", "other", "others", "ought", "our", "ours", "ourself", "ourselves", "several", "she", "some", "somebody", "someone", "something", "somewhat", "such", "suchlike", "that", "thee", "their", "theirs", "theirself", "theirselves", "them", "themself", "themselves", "there", "these", "they", "thine", "this", "those", "thou", "thy", "thyself", "us", "we", "what", "whatever", "whatnot", "whatsoever", "whence", "where", "whereby", "wherefrom", "wherein", "whereinto", "whereof", "whereon", "wherever", "wheresoever", "whereto", "whereunto", "wherewith", "wherewithal", "whether", "which", "whichever", "whichsoever", "who", "whoever", "whom", "whomever", "whomso", "whomsoever", "whose", "whosever", "whosesoever", "whoso", "whosoever", "ye", "yon", "yonder", "you", "your", "yours", "yourself", "yourselves"]


dash_dict = {0: "Выбрать длинное тире", 1: "Выбрать короткое тире"}
quotes_dict = {0: "Выбрать елочки", 1: "Убрать елочки"}
pars_dict = {0: "Отбить абзацы", 1: "Не отбивать абзацы"}
tags_dict = {0: "Добавить теги", 1: "Не добавлять теги"}


def reset_dash():
    global long_dash
    long_dash = not long_dash
    butt_dash.config(text=dash_dict[long_dash])


def reset_quotes():
    global fir_like
    fir_like = not fir_like
    butt_quotes.config(text=quotes_dict[fir_like])


def reset_pars():
    global fix_pars
    fix_pars = not fix_pars
    butt_pars.config(text=pars_dict[fix_pars])


def reset_tags():
    global add_tags
    add_tags = not add_tags
    butt_tags.config(text=tags_dict[add_tags])


import re


def edit_dashes(long_dash, src):
    assert (long_dash in (True, False)), "bool is not bool"
    if long_dash:
        repl = r'— '
    else:
        repl = r'– '
    return re.sub(r'- ', repl, src)


def edit_multispaces(src):  # del multiple spaces
    return re.sub(r' {2,}', r' ', src)


def edit_near_quotes(src):  # «»&“”-only
    return re.sub(r'([^\.])([,\.])([»”])', r'\1\3\2', src)


def isolate_paragraphs(src):  # VK posts only
    return re.sub(r'\n([^–—])', r'\n\n\1', src)


def edit_dialogues(long_dash, src):  # -Blahblah -> – Blahblah
    assert (long_dash in (True, False)), "bool is not bool"
    if long_dash:
        repl = r'\n— '
    else:
        repl = r'\n– '
    return re.sub(r'\n-', repl, src)


def edit_quotes(fir_like,
                src):  # «»- those are yolochki, “”- those may work too, "" - this is the browser shit we get rid of
    # run this before edit_near_quotes()
    if fir_like:
        left_repl = r'«\1'
        right_repl = r'\1»'
    else:
        left_repl = r'“\1'
        right_repl = r'\1”'
    tmp = re.sub(r'"([\w])', left_repl, src)
    return re.sub(r'([\w\?!,\.])"', right_repl, tmp)


def edit_spaces(src):  # tricky one
    tmp1 = re.sub(r'([\?!\.])([^\. \n»”])', r'\1 \2', src)
    tmp2 = re.sub(r'([^ ])([«“\(])', r'\1 \2', tmp1)
    tmp3 = re.sub(r'([»”\),])([^ ])', r'\1 \2', tmp2)
    tmp4 = re.sub(r'([«“\(]) ', r'\1', tmp3)
    tmp5 = re.sub(r' ([»”\),\?!])', r'\1', tmp4)
    tmp5 = re.sub(r'([^ \n])([–—])', r'\1 \2', tmp5)
    tmp5 = re.sub(r'([–—])([^ \n])', r'\1 \2', tmp5)
    return re.sub(r' \.([^\.])', r'.\1', tmp5)


def fix_multidots(src):
    tmp1 = re.sub(r'([^\.])\.\.([^\.])', r'\1...\2', src)
    return re.sub(r'[\.]{4,}', r'...', tmp1)

def split_text(src, lng, mode): # mode == words, sentences, paragraphs
    print('I am running on {0} with {1} lang and {2} mode'.format(src, lng, mode))
    if (mode == 'words'):
        splitter = r'[^a-zA-Z-\']+' if lng=='en' else '[^а-яА-Я-]+'
    if (mode == 'sentences'):
        splitter = r'(?<=[\.?!…])[ \n"]+(?=[A-Z])' if lng=='en' else '(?<=[\.?!…])[ \n–—]+(?=[А-Я])'
    if (mode == 'paragraphs'):
        splitter = r'\n+'
    res = list(filter(None, re.split(splitter, src)))
    return res, len(res)


def search_words(src, lng, lst):
    cnt=0
    wds=[]
    words, l = split_text(src, lng, 'words')
    print (words)
    for w in words:
        print(w)
        if (w.lower() in lst):
            cnt=cnt+1
            wds.append(w)
    return cnt,wds,l

def search_words_butt():
    src = field.get("1.0", "end-1c")
    cnt = 0
    wds = []
    if (LANG == 'ru'):
        cnt, wds,l = search_words(src, LANG, pron_ru)
    else:
        cnt,wds,l=search_words(src, LANG, en_pro_nouns)
    answer.insert(INSERT, 'Contains {0} pronouns out of {2}, such as: {1}'.format(cnt, wds,l))
    return cnt, wds

def check_vowels():
    src = field.get("1.0", "end-1c").lower()
    v = split_text(src, 'ru', 'paragraphs')
    #print("V is "+str(v))
    for i in v[0]:
        #print(i)
        #print(re.findall(r'[ёуеыаоэяию]', i))
        cnt = len(re.findall(r'[ёуеыаоэяию]', i))
        answer.insert(INSERT, i + ' ' + str(cnt)+'\n')
    return



def beautify():
    src = field.get("1.0", "end-1c")
    src = edit_dashes(long_dash, src)
    src = edit_dialogues(long_dash, src)
    src = edit_multispaces(src)
    src = edit_spaces(src)
    if fix_pars:
        src = isolate_paragraphs(src)
    src = edit_quotes(fir_like, src)
    src = edit_near_quotes(src)
    src = fix_multidots(src)
    global result
    if add_tags:
        src += "\n#сказка #городская_сказка #cityhaze\n"
    result = src
    sym_cnt.config(text=str(len(src)))
    answer.insert(INSERT, src)
    return src


from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("GUI на Python")
root.geometry("1000x250")

top=Frame(root)
top.pack(side="top")
bottom=Frame(root)
bottom.pack(side="bottom")

msg = StringVar()
field = Text(width=100, height=20)
field.pack(in_=top)

modeList = StringVar(root)
langList = StringVar(root)

# Dictionary with options
mode = ['words', 'sentences', 'paragraphs']
lang = ['ru', 'en']
modeList.set('words') # set the default option
langList.set('ru')


# on change dropdown value
def change_dropdown(*args):
    global MODE
    MODE = modeList.get()
    print(MODE)

def change_dropdown2(*args):
    global LANG
    LANG = langList.get()
    print(LANG)

modeList.trace('w', change_dropdown)
langList.trace('w', change_dropdown2)

def listSelect():
    src = field.get("1.0", "end-1c")
    txtList, l = split_text(src, LANG, MODE)
    strOut = ''
    #for i in txtList:
    #    strOut= strOut+i+', '
    #strOut= strOut+'\n'
    strOut = strOut +str(l)
    answer.insert(INSERT, strOut)
    ##

from statistics import mean

def sentSplit():
    src=field.get("1.0", "end-1c")
    sent, l_sent = split_text(src, LANG, 'sentences')
    for i in sent:
        answer.insert(INSERT, i+'\n')

def genCount():
    src = field.get("1.0", "end-1c")
    pars, l_pars = split_text(src, LANG, 'paragraphs')
    sent, l_sent = split_text(src, LANG, 'sentences')
    wrd, l_wrd = split_text(src, LANG, 'words')
    l_sym= len(src)
    avg_wrd_len=avg_sent_in_wrd=avg_sent_in_sym=pars_lens=0
    avg_wrd_len=mean(list([len(i) for i in wrd]))
    avg_sent_in_wrd = mean(list([split_text(i, LANG, 'words')[1] for i in sent]))
    avg_sent_in_sym = mean(list([len(i) for i in sent]))
    pars_lens=list([len(split_text(i, LANG, 'sentences')[0] ) for i in pars])

    print('Text contains {0} paragraphs, {1} sentences, {2} words, {3} symbols'.format(l_pars, l_sent, l_wrd, l_sym))
    answer.insert(INSERT, 'Text contains {0} paragraphs, {1} sentences, {2} words, {3} symbols\n'.format(l_pars, l_sent, l_wrd, l_sym))
    print('That is in average {0} symbols per word, {1} symbols or {2} words per sentence\n'.format(avg_wrd_len,avg_sent_in_sym,avg_sent_in_wrd))
    answer.insert(INSERT, 'That is in average {0} symbols per word, {1} symbols or {2} words per sentence\n'.format(avg_wrd_len,avg_sent_in_sym,avg_sent_in_wrd))
    print('And the numbers of sentences per paragraph are: ')
    print(pars_lens)
    answer.insert(INSERT, 'And the numbers of sentences per paragraph are: ')
    answer.insert(INSERT, pars_lens)

    ##
opt1 = OptionMenu(root, modeList, *mode)
opt2 = OptionMenu(root, langList, *lang)
#opt.config(width=90, font=('Helvetica', 12))



opt2.pack(in_=top, side="left")

vow_butt = Button(text="Посчитать слоги", command=check_vowels)
vow_butt.pack(in_=top, side="left")

sent_butt = Button(text="Sentences", command=sentSplit)
sent_butt.pack(in_=top, side="left")

butt_gen = Button(text="Count", command=genCount)
butt_gen.pack(in_=top, side="left")

opt1.pack(in_=top, side="left")

butt_prons = Button(text="Посчитать местоимения", command=search_words_butt)
butt_prons.pack(in_=top, side="left")

butt_options = Button(text="Посчитать", command=listSelect)
butt_options.pack(in_=top, side="left")

butt_dash = Button(text=dash_dict[long_dash], command=reset_dash)
butt_dash.pack(in_=top, side="right")

butt_quotes = Button(text=quotes_dict[fir_like], command=reset_quotes)
butt_quotes.pack(in_=top, side="right")

butt_pars = Button(text=pars_dict[fix_pars], command=reset_pars)
butt_pars.pack(in_=top, side="right")

butt_tags = Button(text=tags_dict[add_tags], command=reset_tags)
butt_tags.pack(in_=top, side="right")

result = ''
editor_butt = Button(text="Make it better", command=beautify)
editor_butt.pack(in_=top)

sym_cnt = Label(text="")
sym_cnt.pack(in_=top)
answer = scrolledtext.ScrolledText(width=100, height=20)

answer.pack(in_=bottom)



root.mainloop()