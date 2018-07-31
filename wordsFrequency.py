#-*- coding: utf-8 -*-

"""
Created on Mon Jul 30 16:44:53 2018

@author: leonardo
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import csv

#read stop words
stopwordsBr = open('stopwords.txt', 'r',encoding='utf-8').read()
#read the txt file
word_list = open('exemplo.txt', 'r',encoding='utf-8').read().split(' ')
#put all words in lowercase
word_list = map(str.lower ,word_list)
#remove stopwords and other stuffs
filtered_words = [word.replace('.','').replace(',', '').replace('\n', '') for word in word_list 
                  if word not in (stopwordsBr)]


wordfreqdist = nltk.FreqDist(filtered_words)
mostcommon = wordfreqdist.most_common(30)

plt.figure(figsize=(15,10))
plt.yticks(range(len(mostcommon)), [val[0] for val in mostcommon])
plt.barh(range(len(mostcommon)),[val[1] for val in mostcommon], align='center')
plt.savefig('mostcommonWords.png')
plt.show()

with open('WordsFrequency.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter='|')
    filewriter.writerow(['Palavra', 'Quantidade'])
    for key in wordfreqdist:
        filewriter.writerow([key,wordfreqdist[key]])

#wordcloud 
#wordcloud = WordCloud(max_words=100    
#                         ).generate('\n'.join(map(str, filtered_words)))
#
#
#
#plt.clf()
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis('off')
#plt.savefig('imageCloud.png',dpi = 100)
#plt.show()
