import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pybtex.database import BibliographyData, Entry
from pybtex.database.input import bibtex
import pandas as pd
import time
import json

import random


def search_doi(doi):
    '''根据doi查论文详细信息'''
    url = f'https://api.crossref.org/works/{doi}'
    response = requests.get(url)
    result = None
    if response.status_code == 200:
        result = response.json()['message']
    else:
        print('Error occurred')
    return result

# doi = 'https://dl.acm.org/doi/abs/10.1145/3394486.3403237'
# result = search_doi(doi)
# print(f"Title: {result['title'][0]}:{result['subtitle'][0]}")
# print(f"Author(s): {', '.join(author['given'] + ' ' + author['family'] for author in result['author'])}")
# print(f"Journal: {result['container-title'][0]}")
# print(f"Publication Date: {result['published-print']['date-parts'][0][0]}")


def search_cite(atid):
    '''根据atid查cite'''
    url = f'https://scholar.google.com/scholar?q=info:{atid}:scholar.google.com/&output=cite&scirp=8&hl=zh-CN'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    result = {}
    for item in soup.find_all('tr'):
        cith = item.find('th', class_='gs_cith').getText()
        citr = item.find('div', class_='gs_citr').getText()
        result[cith] = citr
    return result

# result = search_cite('_goqYZv1zjMJ')
# print(result)



# 更改节点配置
def change_clash_node(node_name=None):
    # Clash API的URL和密码
    url = 'http://127.0.0.1:15043/proxies/🔰国外流量'
    password = 'ee735f4e-59c6-4d60-a2ad-aabd075badb2'
    local_node_name = ['香港1-IEPL-倍率1.0', '香港2-IEPL-倍率1.0', '香港3-IEPL-倍率1.0', 
                       '台湾1-IEPL-倍率1.0', '台湾2-IEPL-倍率1.0', '台湾3-IEPL-倍率1.0',
                       '新加坡1-IEPL-倍率1.0', '新加坡2-IEPL-倍率1.0', '新加坡3-IEPL-倍率1.0'
                       ]
    node_name = node_name or random.choice(local_node_name)
    print(f'当前选择节点名称: {node_name}')
    
    headers = {'Authorization': password}
    data = {
        'name': 'Rule',
        'type': 'Selector',
        'now': node_name
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print('节点已更改为：', node_name)
    else:
        print('更改节点时出错：', response.text)

# 更改节点为my_node
# change_clash_node()



def proxy_requests(url):
    proxies = {
        'http': 'socks5://127.0.0.1:7890',
        'https': 'socks5://127.0.0.1:7890'
    }
    return requests.get(url, proxies=proxies)


def search(title='GNN', start=0):
    url = f'https://scholar.google.com/scholar?start={start}&q=allintitle:+{title}&hl=zh-CN&as_sdt=0,5'
    resp = proxy_requests(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    try:
        papers_item = soup.find(id='gs_res_ccl_mid').find_all('div', class_='gs_scl')
    except:
        print(soup)
        if 'captcha-form' in soup:
            return -1
    papers_info = []
    for paper in papers_item:
        publisher = paper.find('div', class_='gs_or_ggsm').getText().split()[1].split('.')[0]
        href = paper.find('h3', class_='gs_rt').find('a').get('href')
        title = paper.find('h3', class_='gs_rt').find('a').getText()
        detail = paper.find('div', class_='gs_ri').find('div', class_='gs_a').getText()
        year = detail.split(',')[-1].strip()[:4]
        
        # atid = paper.find('h3', class_='gs_rt').find('a').get('data-clk-atid')
        # cite_info = search_cite(atid)['MLA']
        # cite_info_filter = list(filter(lambda x:x, map(lambda x:x.strip().strip('"').strip(), cite_info.strip().split('.'))))
        # author, title, publisher, year = cite_info_filter
        
        papers_info.append({'title':title, 'year':year, 'publisher':publisher, 'href':href})
    return papers_info




index_start = 0
index_end = 500
index_gap = 10
papers_store = []
bar = tqdm(total=index_end-index_start, desc=f'From {index_start} to {index_end}')
# for start in range(index_start, index_end, index_gap):
while index_start < index_end:
    try:
        papers_info = search(title='GNN', start=index_start)
        if papers_info == -1:
            print('需要验证码，更换节点后2秒内重试')
            change_clash_node()
            time.sleep(2)
            continue
        papers_store.extend(papers_info)
    except AttributeError as e:
        print(e)
        break
        
    index_start += index_gap
    bar.update(index_gap)
    bar.refresh()
    time.sleep(0.1)
bar.close()

df = pd.DataFrame(papers_info)
print(df)
df.to_csv('data.csv', index=False)