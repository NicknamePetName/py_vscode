import requests
import re
from urllib import parse
import os

# 起始的目标站点
url = 'https://hifini.com/'
# 构造身份信息
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


# 请求首页URL
def get_list_data(url):
    response = requests.get(url, headers=headers)
    html_data = response.text  # 网页源码
    return html_data


# 解析首页源码 得到歌曲详情页面的URL以及歌名
def parse_data(data):
    z = '<li\sclass="media\sthread\stap\s\s".*?>.*?<div\sclass="media-body">.*?<a\shref="(.*?)">(.*?)</a>'
    result = re.findall(z, data, re.S)
    # print(result)
    for i in result:
        # https://hifini.com/thread-1937.htm
        href = 'https://hifini.com/' + i[0]
        name = i[1]
        print(href)
        print(name)
        print('========' * 7)  # https://hifini.com/get_music.php?key=cAvZ6DyJfeApcbPXJ/zwtMrqBRQURmpyHZya5d4OVNmyhwUPVXK6hdTLbDuH1c+JZae8s6Pd4xAuj4+Ml5dR
        get_song_link(href)

# 像歌曲详情页面发请求 得到歌曲播放资源
def get_song_link(href):
    song_html_data = get_list_data(href)  # 得到详情也得源码
    song_re = "music:\s\[.*?title:\s'(.*?)'.*?url:\s'(.*?)',"
    result = re.findall(song_re, song_html_data, re.S)
    # song_name = re.findall(song_re, song_html_data, re.S)
    for i in result:
        song_name = i[0]
        song_link = i[1]
        print(song_name)
        print("歌曲资源链接：",song_link)
        if not 'https://hifini.com/' in song_link:
            song_url = 'https://hifini.com/' + song_link
            print("歌曲播放资源得链接：",song_url)  # https://m.hifini.com/music/%E8%B5%B7%E9%A3%8E%E4%BA%86%EF%BC%88%E6%97%A7%E7%89%88%EF%BC%89.m4a

            # 像歌曲播放链接再次发请求 获得二进制数据
            data_byts = requests.get(song_url,headers=headers).content  # 得到歌曲二进制数据

            # 判断文件夹是否存在
            if not os.path.exists('歌单'):
                # 不存在则创建
                os.makedirs('歌单')
            song_name = re.sub('[\/:?*"<>|]','-',song_name)
            with open('歌单\{}.m4a'.format(song_name),'wb')as f:
                f.write(data_byts)

if __name__ == '__main__':
    html_data = get_list_data(url)
    # print(html_data)
    parse_data(html_data)
