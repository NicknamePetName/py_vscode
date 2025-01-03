import requests
import re

# 发请求


def getData(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    }

    res = requests.get(url, headers=headers,allow_redirects=False)
    print(res.text)
    if res.status_code == 200:
        return res.text
    return None


# 解析数据


def parseData(data):
    if data == None:
        return None

    regular = '<li\sclass="news-meta-item.*?href="(.*?)"\starget="_blank">' \
    '.*?<span\sclass="title-content-title">(.*?)</span>'
    result = re.findall(regular, data, re.S)
    print(result)
    return result

def printData(result):
    for item in result:
        print(item[1])
        print(item[0])


# if __name__ == "main":
url = "https://www.baidu.com/"
data = getData(url)
result = parseData(data)
printData(result)

