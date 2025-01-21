import requests
import json
import os
import csv
import re
import copy
import logging
import traceback
import time
import tkinter as tk
from tkinter import simpledialog

# 配置日志记录
logging.basicConfig(filename='yixin-product.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',encoding='utf-8')
def get_input():
    # 创建主窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 获取参数
    info = simpledialog.askstring("Input", "请输入参数-info:").strip()
    sign = simpledialog.askstring("Input", "请输入参数-sign:").strip()
    userid = simpledialog.askstring("Input", "请输入参数-userId:").strip()
    data = simpledialog.askstring("Input", "请输入参数-data:").strip()
    # 返回获取的参数
    return info, sign, userid, data


info, sign, userid, data = get_input()



headers_text = {
    'Content-Type': 'text/plain',
    'Connection': 'keep-alive',
    'Host': '127.0.0.1:13301',
    'Source-Type': '1',
    'client_session': 'YLCqDKwc7HzjrLRk+E7qQt8z+Iwhpb6UD22aIBW2dX0=',
    'info': info,
    'sign': sign,
    'userid': userid
}



product_data = {
    'task_id': '',
    'goods_id': '',
    'stock': ''
}


product_list = []
productURL = 'http://127.0.0.1:13301/hospital%2fmanage%2fnew_stock_statistics'
logging.info('发起请求')
response = requests.post(productURL, data=data, headers=headers_text)

logging.info(response.text)


responseData = json.loads(response.text)['Data']
if not isinstance(responseData,list):
    responseData = []



for product in responseData:
    product_data_copy = copy.deepcopy(product_data)
    product_data_copy['goods_id'] = product['con_commodity_id']
    product_data_copy['stock'] = product['quantity']
    product_list.append(product_data_copy)


if not os.path.exists('医院数据'):   # 不存在则创建
    # 创建文件夹
    os.makedirs('医院数据')
csv_file_product = './医院数据/商品库存信息.csv'
# 检查文件是否存在且不为空
file_exists = os.path.isfile(csv_file_product) and os.path.getsize(csv_file_product) > 0
# 保存到.csv文件中
print('保存数据到商品库存信息中···')

with open(csv_file_product,'a',encoding='utf-8',newline='') as f:
    # 将文件对象转换成 DictWriter 对象
    writer = csv.DictWriter(f,fieldnames = product_data.keys())
    # 如果文件是新创建的，写入表头
    if not file_exists:
        writer.writeheader()
    writer.writerows(product_list)


print("数据导出完毕！！!")
logging.info("数据导出完毕！！!")
os.system("pause")