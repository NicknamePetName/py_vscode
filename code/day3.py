import requests
import re
import os


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


def req_get_url(url):
    response = requests.get(url, headers=headers)
    return response.text  # 网页源码


def parse_data(html_data):
    page_regura = '<li\sclass="media\sthread\stap\s\s".*?<div\sclass="subject\sbreak-all">.*?<a\shref="(.*?)">(.*?)</a>'
    page_list = re.findall(page_regura, html_data, re.S)
    j = 1
    for i in page_list:
        song_href = 'https://hifini.com/' + i[0]
        song_name = re.sub('\[.*?\]','',i[1])
        song_name = re.sub('[\/:*?"<>|]','-',song_name)

        music_html = req_get_url(song_href) # 音乐详情页面
        music_regura = 'music:\s\[.*?url:\s\'(.*?)\','  # 获取音乐地址的正则表达式
        music_href = re.findall(music_regura,music_html,re.S)

        if not music_href:  # 防止歌曲链接为空
            continue
        elif 'https://hifini.com/' not in music_href:
            music_href = 'https://hifini.com/' + music_href[0]

        song_data = requests.get(music_href,headers=headers).content

        # 保存歌曲到本地
        with open(f'歌单\{song_name}.m4a','wb') as f:
            f.write(song_data)


if __name__ == '__main__':
    if not os.path.exists('歌单'): # 不存在则创建
        # 创建文件夹
        os.makedirs('歌单')
    for page in range(1,10864):
        url = f'https://hifini.com/index-{page}.htm'
        parse_data(req_get_url(url))


