# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:55:13 2018

@author: leonardot
"""

import csv
import nltk
import string
import unicodedata
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')


def clean_csv(file):
    
    csv_words = []
    with open(file, 'r',encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            str1 = ''
            row_splited = nltk.word_tokenize(str1.join(row))
            for word in row_splited:
                wordD = str(word).lower().strip(string.punctuation)
                wordD = remove_diacritic(wordD).decode()
                csv_words.append(wordD)
            
    return csv_words
    

def plot_commonWords(mostcommon,filepath = 'mostcommonWords.png'):
    
    plt.figure(figsize=(15,10))
    plt.yticks(range(len(mostcommon)), [val[0] for val in mostcommon])
    plt.barh(range(len(mostcommon)),[val[1] for val in mostcommon], align='center')
    plt.savefig(filepath)
    plt.show()
    
    
def save_words_frequency_csv(wordfreqlist, filepath= 'WordsFrequency.csv'):
    with open(filepath, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter='|')
        filewriter.writerow(['Palavra', 'Quantidade'])
        for key in wordfreqlist:
            filewriter.writerow([key,wordfreqlist[key]])
            

def generate_wordcloud(filtered_words,maxwords=30):
    wordcloud = WordCloud(max_words=maxwords    
                         ).generate(' '.join(map(str, filtered_words)))
    plt.clf()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('imageCloud.png',dpi = 100)
    plt.show()
    

def get_stopwords():
    stopwords = []
    file = open('stopwords.txt', 'r',encoding='utf-8')
    for word in file:
        stopwords.append(remove_diacritic(word).decode().lower().strip(string.punctuation).replace('\n', '').replace(' ', ''))
    return stopwords
    

def deal_csv(file):
    
    stopwordsBr = get_stopwords()
    word_list = clean_csv(file)
    
    filtered_words = [word.replace('.','').replace(',', '').replace('\n', '') for word in word_list 
                  if( word not in stopwordsBr 
                      and len(word) > 3) 
                      and not word.isdigit()]
    
    wordfreqlist = nltk.FreqDist(filtered_words)
    mostcommon = wordfreqlist.most_common(30)
    plot_commonWords(mostcommon)
    save_words_frequency_csv(wordfreqlist)
    generate_wordcloud(filtered_words)
    

deal_csv('exemplo.csv')

 
