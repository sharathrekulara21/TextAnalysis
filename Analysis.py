import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
import syllapy
import re
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
import gdown

def positive_score(filename,data):
    score = 0
    with open(filename,'r') as f:
        positive_words = f.read()
    with open(data,'r') as f:
        ip = f.read()
    words = word_tokenize(positive_words)
    input_words = word_tokenize(ip)
    for word in input_words:
        if word in words:
            score+=1
    return score
def negative_score(filename,data):
    score = 0
    with open(filename,'r') as f:
        negative_words = f.read()
    with open(data,'r') as f:
        ip = f.read()
    words = word_tokenize(negative_words)
    input_words = word_tokenize(ip)
    for word in input_words:
        if word in words:
            score-=1
    return score

def polarity_score(pos_score,neg_score):
    ps = (pos_score - neg_score)/((pos_score+neg_score)+0.000001)
    return ps

def word_count(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    words = word_tokenize(ip)
    filtered_words = [w for w in words if not w.lower() in set(stopwords.words('english'))]
    return len(filtered_words)

def subjectivity_score(pos_score,neg_score,input_data):
    sub_score = (pos_score + neg_score)/ ((word_count(input_data))+0.000001)
    return sub_score

def avg_sent_length(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    sentences = sent_tokenize(ip)
    return word_count(input_data)/len(sentences)

def percentage_complex_words(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    words = word_tokenize(ip)
    complex_words = [w for w in words if syllapy.count(w)>2]
    return len(complex_words)/word_count(input_data)

def fog_index(avg_sen_len,per_comp_words):
    return 0.4*(avg_sen_len + per_comp_words)

def avg_words_sent(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    sentences = sent_tokenize(ip)
    return word_count(input_data)/len(sentences)

def comp_word_count(per_comp_words,word_c):
    return per_comp_words*word_c

def syllable_per_word(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    words = word_tokenize(ip)
    c = 0
    for word in words:
        c+=syllapy.count(word)
    return c/len(words)

def personal_pronouns(input_data):
    pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
    with open(input_data,'r') as f:
        ip = f.read()
    pro = pronounRegex.findall(ip)
    return len(pro)

def avg_word_length(input_data):
    with open(input_data,'r') as f:
        ip = f.read()
    words = word_tokenize(ip)
    c = 0
    for w in words:
        c+=len(w)
    return c/len(words)

gdown.download("Inset the google drive links for the positive-words",fuzzy=True)
gdown.download("Insert drive link","negative-words.txt",fuzzy=True)
input_data = pd.read_csv("Input.csv")
output_data = pd.read_excel("Output Data Structure.xlsx")
for i in range(len(input_data)):
    url_id = input_data.iloc[i,0]
    url = input_data.iloc[i,1]
    res = requests.get("{}".format(url))
    try:
        soup = BeautifulSoup(res.text,"html.parser")
        paragraphs = soup.find('div', attrs={"class":"td-post-content"}).text
        with open('{}.txt'.format(url_id), 'w',encoding='cp437',errors='ignore') as f:
            f.write(paragraphs)
        pos_score = positive_score("positive-words.txt","{}.txt".format(url_id))
        neg_score = negative_score("negative-words.txt","{}.txt".format(url_id))
        pol_score = polarity_score(pos_score,neg_score)
        sub_score = subjectivity_score(pos_score,neg_score,'{}.txt'.format(url_id))
        avg_sen_len = avg_sent_length('{}.txt'.format(url_id))
        per_comp_words = percentage_complex_words('{}.txt'.format(url_id))
        f_ind = fog_index(avg_sen_len,per_comp_words)
        avg_word_per_sen = avg_words_sent('{}.txt'.format(url_id))
        word_c = word_count('{}.txt'.format(url_id))
        complex_words_count = comp_word_count(per_comp_words,word_c)
        syllb_per_word = syllable_per_word('{}.txt'.format(url_id))
        per_pronouns = personal_pronouns('{}.txt'.format(url_id))
        avg_w_len = avg_word_length('{}.txt'.format(url_id))
    except AttributeError:
        pos_score = None
        neg_score = None
        pol_score = None
        sub_score = None
        avg_sen_len = None
        per_comp_words = None
        f_ind = None
        avg_word_per_sen = None
        word_c = None
        complex_words_count = None
        syllb_per_word = None
        per_pronouns = None
        avg_w_len = None
    
    output_data.iloc[i,2] = pos_score
    output_data.iloc[i,3] = neg_score
    output_data.iloc[i,4] = pol_score
    output_data.iloc[i,5] = sub_score
    output_data.iloc[i,6] = avg_sen_len
    output_data.iloc[i,7] = per_comp_words
    output_data.iloc[i,8] = f_ind
    output_data.iloc[i,9] = avg_word_per_sen
    output_data.iloc[i,10] = complex_words_count
    output_data.iloc[i,11] = word_c
    output_data.iloc[i,12] = syllb_per_word
    output_data.iloc[i,13] = per_pronouns
    output_data.iloc[i,14] = avg_w_len
    output_data.to_excel("Output Data Structure.xlsx")
    
