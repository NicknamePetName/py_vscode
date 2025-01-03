from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import os
import re


opts = Options()
opts.add_argument('--headless')
opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options = opts)
driver.maximize_window()
headers = {
    'User_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


class_list = [] # 类名
# 获取需要爬取的药 
response = requests.get('https://www.qihuang.vip/fang.php',headers=headers)
bs_book = BeautifulSoup(response.text,'html.parser')
h2_tags = bs_book.find_all('h2')
for h2_tag in h2_tags:
    class_list.append(h2_tag.text[:3])

is_login = True # 登录，验证身份，,每次启动都要登录


for i in range(1,20):  #   这里改变的是第几大类0-11
    # 爬取的大类
    kind_name = class_list[i]
    class_book = f'category_fang_{i}'
    class_ = bs_book.find('div',id = class_book)
    tr_s = class_.find_all('tr')
    
    for tr in tr_s:
        a_list = [] #药列表
        tr_classify = tr.find('td', class_ = 'classify').text
        tr_yao_a_s = tr.find('td', class_ = 'yao').find_all('a')
        for a in tr_yao_a_s:
            a_list.append(a['href'])

        # 在这里创建文件夹，接下来后续步骤
        
        file_ = '方剂选粹' + '/'+ kind_name + '/' + tr_classify
        
        if not os.path.exists(file_):   # 不存在则创建
        # 创建文件夹
            os.makedirs(file_)
        
        for href in a_list:
            driver.get(f'https://www.qihuang.vip/{href}')
            if is_login: # 登录凭证
                username = driver.find_element(By.ID,'ls_username')
                password = driver.find_element(By.ID,'ls_password')
                username.send_keys('nickname')
                password.send_keys('cannian.zn.c0m')
                button = driver.find_element(By.TAG_NAME,'button')
                button.click()
                time.sleep(5)   # 需要加载一会儿
                is_login = False


            html = driver.page_source
            bs = BeautifulSoup(html,'html.parser')
            headline = bs.find('div', id = 'headline').text[1:]
            print('正在爬取： ' + file_ + '/'+ headline)  #title
            content = bs.find('div',id = 'content').text[:-6]
            
            with open(file_ + '/' + headline + '.txt','a',encoding='utf-8') as f:
                f.write(content)
        
        print(tr_classify + '爬取完成')

driver.quit()
