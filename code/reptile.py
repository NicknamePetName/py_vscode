"""爬虫语法"""
# 代理————快代理  隧道代理，独享代理
# 引入requests包，发起http/https请求
import json
import requests
# 异常，超时异常
from requests.exceptions import Timeout

URL = "https://hifini.com/"  # 请求地址，路径

# 伪装身份信息，身份信息可以放入多条
headers = {
    # 伪装浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    # 用户信息(userName+Password) 只是维持登录状态
    # 好处：可以爬取需要登录才能获取的网站
    # 坏处：大大提高了你被反爬的几率 （封号）
    "Cookie": "oMVX_2132_lastcheckfeed=1290344%7C1699883640; oMVX_2132_nofavfid=1; oMVX_2132_smile=5D1; oMVX_2132_visitedfid=360D378D173D380; oMVX_2132_ulastactivity=1d96Xj2z9PPjMETFQH%2By%2B%2FKr%2FAj0zmnLtgrExaGVPW3%2FsN0oBaYe; oMVX_2132_saltkey=e5Zh3h4n; oMVX_2132_lastvisit=1703342993; acw_tc=2f624a5317035062226685394e12cdc28d93c8b59be602696c70d41b15b269; oMVX_2132_atarget=1; oMVX_2132_sid=ma99pP; oMVX_2132_st_t=0%7C1703507606%7C2fa6a7a1c880a3f0a71409931791cbce; oMVX_2132_forum_lastvisit=D_360_1703507606; oMVX_2132_lastact=1703507606%09home.php%09misc; oMVX_2132_sendmail=1",
}

# 构造ip信息，（代理）
ip = {
    'http': '202.55.5.209:8090',
    'https': '2020.55.5.209:8090',
}

# get方法请求的参数
get = {"name": "lisi", "age": 18, "age2": 21}

# 发起get请求,timeout设置超时参数，parmas携带get请求参数,headers携带身份信息,proxies:挂代理，防止服务器封ip
req = requests.get(URL, timeout=1, params=get, headers=headers,proxies=ip)

print(req)
print(req.text)  # 响应内容

req = req.encoding("utf-8")  # 指定编码，解码

print(type(req))  # 请求类型
print(type(req.text))  # text请求类型

print(req.status_code)  # 打印状态码

json_data = json.loads(req.text)  # 将str转为dict

data1 = req.content  # .content获取二进制数据


# post方法请求参数
post = {
    "name": "lisi",
}
# 发起post请求,data作用是携带post请求参数,allow_redirects为False禁止网页跳转（重定向，状态码301）
try: #处理异常
    req2 = requests.post(URL, timeout=1, data=post, allow_redirects=False,proxies=ip)
except Timeout: #出现异常怎么处理
    print('timeout超时')

print(req.headers)  # 查看响应头信息

print(req.url)  # 查看url

print(req.history)  # 查看网页是否跳转


# 通过session 让服务器知道是上一次的你
ses = requests.session() # 实例化
res = ses.get(URL)
