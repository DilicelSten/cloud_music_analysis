# -*-coding:utf-8 -*-
"""
created on:2017/10/6
author:DilicelSten
target:从薛之谦的50首歌词中切词并统计词频制作词云
finished on:2017/10/6
"""
import jieba.analyse
import os
from os import path
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud,ImageColorGenerator


d = path.dirname(__file__)  # 为代码路径

all_words = []
ipath = '../lyrics/'
lyrics = ''

stopwords = [line.strip().decode('gbk') for line in open('stop_words.txt').readlines()]
for filename in os.listdir(ipath):
    # print (filename)
    with open(ipath + filename, 'r') as f:
        lyrics += f.read().decode('utf-8')
# print (lyrics)
result = jieba.analyse.textrank(lyrics, topK=1000, withWeight=True)  # 基于TextRank算法的关键词提取前1000个
# print result[0][0]
keywords = dict()
for i in result:
    if i[0] not in stopwords:#去停用词
        keywords[i[0]] = i[1]
    else:
        print '有停用词'

backgroud_Image = imread(path.join(d, "timg3.jpg"))
# 词云
wc = WordCloud(
                background_color='white',    # 设置背景颜色
                mask=backgroud_Image,        # 设置背景图片
                max_words=8000,            # 设置最大显示的字数
                font_path='msyh.ttc',      # 设置字体格式，如不设置显示不了中文
                max_font_size=50,            # 设置字体最大值
                random_state=100,            # 设置有多少种随机生成状态，即有多少种配色方案

                )
wc.generate_from_frequencies(keywords)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file(path.join(d, "cloud graph.png"))
