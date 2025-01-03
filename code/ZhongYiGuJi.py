from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import os

opts = Options()
opts.add_argument('--headless')
opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options = opts)
driver.maximize_window()
headers = {
    'User_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


book_list = []  # 书籍列表
# 获取需要爬取的书籍 (方药部分)
response = requests.get('https://www.qihuang.vip/book.php',headers=headers)
bs_book = BeautifulSoup(response.text,'html.parser')
category_book_1 = bs_book.find('div',id = 'category_book_1')
strong_tags = category_book_1.find_all('strong')
for strong in strong_tags:
    a_book_href = strong.find('a')['href']
    book_list.append(a_book_href)

is_login = True # 登录，验证身份

if not os.path.exists('中药1'):   # 不存在则创建
    # 创建文件夹
    os.makedirs('中药1')


for book in book_list:
    driver.get(f"https://www.qihuang.vip/{book}") # 发起请求
    # driver.get(f"https://www.qihuang.vip/book-{book}.html")

    if is_login: # 登录凭证
        username = driver.find_element(By.ID,'ls_username')
        password = driver.find_element(By.ID,'ls_password')
        username.send_keys('nickname')
        password.send_keys('cannian.zn.c0m')
        button = driver.find_element(By.TAG_NAME,'button')
        button.click()
        time.sleep(5)   # 需要加载一会儿
        is_login = False 
    
    tag_id_ct = driver.find_element(By.ID,'ct')
    book_name = tag_id_ct.find_element(By.TAG_NAME,'h1').find_element(By.TAG_NAME,'a').text  # 书籍名称
    print(f'\n\n开始爬取: ' + book_name +'\n\n')
    html = driver.page_source

    bs = BeautifulSoup(html,'html.parser')
    catalog_id = bs.find('div',id = 'catalog')


    # 爬取第一个h3节点之前的所有strong标签的所有内容
    h3_first = catalog_id.find('h3')
    print(h3_first)
    if h3_first:
        strongss = []
        for sibling in h3_first.previous_siblings:
            if sibling.name == 'strong':
                strongss.append(sibling)
        

        for strongs in reversed(strongss):

            a_h3_first = strongs.find('a')

            # 判断strong标签中的a标签是否为空
            if not a_h3_first.text: 
                continue

            a_h3_href = 'https://www.qihuang.vip/' + a_h3_first['href']

            driver.get(a_h3_href)
            res_html = driver.page_source
            bs_a = BeautifulSoup(res_html,'html.parser')

            
            headline_id_name = '\n' + bs_a.find('div',id = 'headline').text + '  ***************************' # 章节名称
            print('      爬取' + bs_a.find('div',id = 'headline').text + 'ing')
            view_id = bs_a.find('div',id = 'view') 
            content = view_id.text # 章节内容
            with open(f'./中药1/{book_name}.txt','a',encoding='utf-8') as f:
                f.write(headline_id_name)
                f.write(content[:-6])
    else:
        strong_all = catalog_id.find_all('strong')
        for strongs in strong_all:
            a_h3_first = strongs.find('a')
            a_h3_href = 'https://www.qihuang.vip/' + a_h3_first['href']

            driver.get(a_h3_href)
            res_html = driver.page_source
            bs_a = BeautifulSoup(res_html,'html.parser')
            headline_id_name = '\n' + bs_a.find('div',id = 'headline').text + '  ***************************' # 章节名称
            print('      爬取' + bs_a.find('div',id = 'headline').text + 'ing')
            view_id = bs_a.find('div',id = 'view') 
            content = view_id.text # 章节内容
            with open(f'./中药1/{book_name}.txt','a',encoding='utf-8') as f:
                f.write(headline_id_name)
                f.write(content[:-6])



    h3_tags = catalog_id.find_all('h3')
    for h3 in h3_tags:
        print('正在爬取：' + h3.text )
        class_name = '\n\n' + h3.text + '  ——————————————————————————————————————————————————————————————————————————————————————————\n' # 分类名称
        with open(f'./中药1/{book_name}.txt','a',encoding='utf-8') as f:
            f.write(class_name)
        for sibling in h3.find_next_siblings():
            if sibling.name != 'strong':
                break
            a_tag = sibling.find('a')
            if not a_tag.text:
                continue
            a_href = 'https://www.qihuang.vip/' + a_tag['href']  # 节点链接

            driver.get(a_href)
            res_html = driver.page_source
            bs_a = BeautifulSoup(res_html,'html.parser')
            
            headline_id_name = '\n' + bs_a.find('div',id = 'headline').text + '  ***************************' # 章节名称
            print('      爬取' + bs_a.find('div',id = 'headline').text + 'ing')
            view_id = bs_a.find('div',id = 'view') 
            content = view_id.text # 章节内容
            with open(f'./中药1/{book_name}.txt','a',encoding='utf-8') as f:
                f.write(headline_id_name)
                f.write(content[:-6])
        print( h3.text + ': 爬取完成!')
    
driver.quit()
    

            
            