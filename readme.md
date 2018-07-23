# Netease's cloud music anaylsis
Crawling top 50 music lyrics of xuezhiqian and analysing the number of words he used to see what he really like to express, which I find it interesting in a blog I see.

## Main codes
* crawl_music.py
crawling music lyrics through the links
* analysis.py
spliting the sentences, removing the stop words and then computing the number of words. Finally we can see the word cloud.

## Operating environment
Based on python2.7

* jieba
* matplotlib
* scipy
* wordcloud
* requests
* BeautifulSoup
* re
* json

## Operation instructions
* first step
using the crawl_music.py to store music lyrics in directory:lyrics
* second step
using the analysis.py to analyze and get the wordcloud




