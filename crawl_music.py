# -*- coding:utf-8 -*-
"""
created on:2017/10/3
author:DilicelSten
target:爬取网易云音乐的薛之谦的top50音乐歌词
finished on:2017/10/5
"""
import requests
from bs4 import BeautifulSoup
import json
import re


def get_music_ids_by_singer_id(singer_ID):
    """
    获取这个歌手的歌曲的id
    :param singer_ID: 歌手id
    :return:
    """
    url = 'http://music.163.com/artist?id=' + str(singer_ID)
    r = requests.get(url).text
    # print(r)
    bs_obj = BeautifulSoup(r, 'lxml')  # 添加lxml解析器
    # print bs_obj.body
    singer_name = bs_obj.select("#artist-name")
    singer_name = singer_name[0].get('title')
    t = bs_obj.find('textarea')  # 找到元素
    # print t
    # print t.text.replace('(', '[').replace(')', ']').replace('\'', '"')
    musics = json.loads(t.text.replace('(', '[').replace(')', ']').replace('\'', '"'))
    # print musics
    ids = {}
    for music in musics:
        ids[music['name']] = music['id']
    return ids, singer_name


def get_lyric_by_music_id(music_id):
    """
    通过音乐的id得到歌词
    :param music_id:音乐id
    :return:
    """
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    #print(json_obj)
    j = json.loads(json_obj)
    #print(type(j))#打印出来j的类型是字典
    try:#部分歌曲没有歌词，这里引入一个异常
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')#下面这三行正则匹配删除时间轴
        lrc = re.sub(pat,"",lrc)
        lrc = lrc.strip()
        return lrc
    except KeyError as e:
        pass


(music_id_set, singer_name_all) = get_music_ids_by_singer_id(5781)
print(music_id_set)
for key in music_id_set:
    lrc_content = get_lyric_by_music_id(music_id_set[key])
    # print(lrc_content)
    print(key)#歌名
#     #print(singer_name)
#     f = open('../xuezhiqian/data/'+key + '.txt', 'w')
#     try:  # 引入异常
#         #print(type(lrc_content.encode('utf-8')))
#         f.write(lrc_content.encode('utf-8'))
#         # print lrc_content.encode('utf-8')
#         print 'ok'
#         f.close()
#     except AttributeError as e2:
#         pass





