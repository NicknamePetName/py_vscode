import requests
import json
import os
import csv
import re
import copy

'''
    1.会员卡问题
'''

# info = input('请输入参数-info:')
# sign = input('请输入参数-sign:')
# userid = input('请输入参数-userId:')

info = 'GBZa3ajLfh|VrAGvMjLwd'
sign = '0005d5b1b4187661204abb15184604ad'
userid = '1'

# 一杨
# info = 'vzfEEqkUjG|RymcKz9JmF'
# sign = 'e4aea2eba51e1dfc5f582d9387c58f06'
# userid = '14'
print('开始采集数据！！！')

user_data = {
    'task_id': '',
    'owner_id': '',
    'owner_name': '',
    'owner_gender': '',
    'owner_vip_level': '',
    'owner_phone1': '',
    'owner_phone2': '',
    'owner_deposit': '',
    'owner_integral': '',
    'owner_address': '',
    'owner_reg_date': '',
    'owner_remarks': '',
    'owner_source': '',
    'sale_state': '',
    'is_customer': '',
    'hospital_id': '',
    'hospital_code': '',
    'hospital_name': ''
}
    
pet_data = {
    'task_id': '',
    'owner_id': '',
    'pet_id': '',
    'pet_name': '',
    'category': '',
    'kind': '',
    'gender': '',
    'birthday': '',
    'addday': '',
    'weight': '',
    'sterilization': '',
    'repellent': '',
    'vaccines': '',
    'is_dead': '',
    'record_no': '',
    'pet_color': '',
    'hospital_id': '',
    'hospital_code': '',
    'hospital_name': '',
}

card_data = {
    'task_id': '',
    'owner_id': '',
    'card_name': '',
    'card_money': '',
    'card_gift': '',
    'add_date': '',
    'remark': '',
    'create_time': '',
    'type': '',
    'meter': '',
    'overtime': '',
    'opentime': '',
    'off': '',
    'code': '',
    'hospital_id': '',
    'hospital_code': '',
    'hospital_name': '',
}

product_data = {
    'task_id': '',
    'goods_code': '',
    'sale_state': '',
    'name': '',
    'common_name': '',
    'forshort': '',
    'print_name': '',
    'spec': '',
    'barcode': '',
    'category1': '',
    'category2': '',
    'category3': '',
    'category4': '',
    'cost_price': '',
    'sale_price': '',
    'unit': '',
    'dosageunit': '',
    'allow_addcountcard': '',
    'is_calculating_store': '',
    'safe_store': '',
    'use_method': '',
    'printlable': '',
    'drug_message': '',
    'drug_tips': '',
    'manufacturer': '',
    'brand_name': '',
    'license_number': '',
    'remark': '',
    'supplier': '',
    'inspection_name': '',
    'inspection_brand': '',
    'inspection_model': '',
    'stock': ''
}

headers = {
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Host': '127.0.0.1:13301',
    'Source-Type': '1',
    'client_session': 'YLCqDKwc7HzjrLRk+E7qQt8z+Iwhpb6UD22aIBW2dX0=',
    'info': info,
    'sign': sign,
    'userid': userid
}

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
headURL = 'http://127.0.0.1:13301/'


# 去除 windows 操作系统不否和文件命名的字符
def replace_special_chars(text):
    # 定义一个正则表达式，匹配所有不允许的字符
    pattern = r'[<>:"/\\|?*]'
    
    # 使用re.sub替换这些字符为'-'
    return re.sub(pattern, '-', text)



# 获取所有顾客信息（GET) http://127.0.0.1:13301/daily%2fwork%2fhis_consumer
URL_all = headURL + 'daily%2fwork%2fhis_consumer'
response = requests.get(URL_all,headers=headers)  

# text转化为 python 对象
customer_data = json.loads(response.text)

if not os.path.exists('医院数据'):   # 不存在则创建
    # 创建文件夹
    os.makedirs('医院数据')

# 将顾客信息写入customer.json中
with open(f'./医院数据/customer_all.json','w',encoding='utf-8') as f:
    f.write(response.text)


# 获取客户信息
def getCustomerData(customer,user_data,pet_data,card_data):

    file_ = '医院数据/客户信息/' + str(customer['id']) + '-' + replace_special_chars(customer['name'].strip())
    if not os.path.exists(file_):   # 不存在则创建
    # 创建文件夹
        os.makedirs(file_)

    
    # 接口 1 响应体 （GET) http://127.0.0.1:13301/daily%2fwork%2fconsumer%2f19  --------------------------------------------------
    URL_2 = headURL + 'daily%2fwork%2fconsumer%2f' + str(customer['id'])
    customerInfoResponse2 = requests.get(URL_2,headers=headers)

    # 组装数据到 user_data 中
    customerInfoData = json.loads(customerInfoResponse2.text)['Data']
    user_data_copy = copy.deepcopy(user_data)  # 深拷贝
    # task_id 老子不知道
    user_data_copy['owner_id'] = customerInfoData['id'] # 客户ID
    user_data_copy['owner_name'] = customerInfoData['name'] # 客户名称
    user_data_copy['owner_gender'] = customerInfoData['sex'] # 性别 0-未知 1-男  2-女
    # wner_vip_level 会员级别   参数无
    user_data_copy['owner_phone1'] = customerInfoData['telephone'] # 客户手机号
    user_data_copy['owner_phone2'] = customerInfoData['back_up_telephone'] # 客户备用手机号
    user_data_copy['owner_deposit'] = customerInfoData['deposit_money'] # 客户押金
    user_data_copy['owner_integral'] = customerInfoData['bonus'] # 客户积分
    user_data_copy['owner_address'] = customerInfoData['address'] # 客户地址
    user_data_copy['owner_reg_date'] = customerInfoData['add_time'] # 客户注册时间
    user_data_copy['owner_remarks'] = customerInfoData['consumer_tags'] # 客户备注 []
    user_data_copy['owner_source'] = customerInfoData['understand'] # 客户来源
    user_data_copy['sale_state'] = customerInfoData['is_black_list'] # 是否拉黑(正常)  0-正常(否) 1-删除(是)
    # is_customer 是否散客   参数无  0-否，1-是
    user_data_copy['hospital_id'] = customerInfoData['hospital_id']
    user_data_copy['hospital_code'] = customerInfoData['hospital_code']
    user_data_copy['hospital_name'] = customerInfoData['hospital_name']
    

    csv_file = './医院数据/用户数据.csv'
    # 检查文件是否存在且不为空
    file_exists = os.path.isfile(csv_file) and os.path.getsize(csv_file) > 0
    # 保存到.csv文件中
    with open(csv_file,'a',encoding='utf-8',newline='') as f:
        # 将文件对象转换成 DictWriter 对象
        writer = csv.DictWriter(f,fieldnames = user_data.keys())
        # 如果文件是新创建的，写入表头
        if not file_exists:
            writer.writeheader()
        writer.writerow(user_data_copy)

    with open(f'./' + file_ + '/customer2.json','w',encoding='utf-8') as f:
        f.write(customerInfoResponse2.text)


    '''3.0版本变动 （GET）http://127.0.0.1:13301/daily%2fwork%2fcardswithretreat%2f19 '''
    # 接口 2 响应体 （GET) http://127.0.0.1:13301/daily%2fwork%2fcards%2f19  -----------------------------------------------------
    URL_1 = headURL + 'daily%2fwork%2fcards%2f' + str(customer['id'])
    customerInfoResponse1 = requests.get(URL_1,headers=headers)

    # 组装数据到 card_data 中
    cardInfoDataList = json.loads(customerInfoResponse1.text)['Data']
    for cardInfoData in cardInfoDataList:
        card_data_copy = copy.deepcopy(card_data)  # 深拷贝
        # task_id 老子不知道
        card_data_copy['owner_id'] = customer['id'] # 客户ID
        card_data_copy['card_name'] = cardInfoData['con_card_type_name'] # 折扣卡名称
        card_data_copy['card_money'] = cardInfoData['money'] # 本金
        card_data_copy['card_gift'] = cardInfoData['present_money'] # 增额
        card_data_copy['add_date'] = cardInfoData['create_time'] # 创建时间
        # remark 备注 参数无
        card_data_copy['create_time'] = cardInfoData['create_time'] # 创建时间
        card_data_copy['type'] = cardInfoData['type'] # 卡类型 1-折扣卡 2-次卡
        card_data_copy['meter'] = cardInfoData['meter'] # 次卡剩余次数
        card_data_copy['overtime'] = cardInfoData['overtime'] # 次卡到期时间
        card_data_copy['opentime'] = cardInfoData['opentime'] # 次卡开卡时间
        card_data_copy['off'] = cardInfoData['off'] # 折扣卡，折扣范围0-10
        card_data_copy['code'] = cardInfoData['code'] # 卡号
        card_data_copy['hospital_id'] = customerInfoData['hospital_id']
        card_data_copy['hospital_code'] = customerInfoData['hospital_code']
        card_data_copy['hospital_name'] = customerInfoData['hospital_name']


        csv_file = './医院数据/用户卡信息.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file) and os.path.getsize(csv_file) > 0
        # 保存到.csv文件中
        with open(csv_file,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = card_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerow(card_data_copy)


    with open(f'./' + file_ + '/customer1.json','w',encoding='utf-8') as f:
        f.write(customerInfoResponse1.text)

    
    # 接口 3 响应体 （GET) http://127.0.0.1:13301/daily%2fwork%2fpets%2f19  -------------------------------------------------------------
    URL_3 = headURL + 'daily%2fwork%2fpets%2f' + str(customer['id'])
    customerInfoResponse3 = requests.get(URL_3,headers=headers)

    petInfoDataList = json.loads(customerInfoResponse3.text)['Data']
    for petInfoData in petInfoDataList:
        # 组装数据到 pet_data 中
        pet_data_copy = copy.deepcopy(pet_data)  # 深拷贝
        # task_id 老子不知道
        pet_data_copy['owner_id'] = customer['id'] # 客户ID
        pet_data_copy['pet_id'] = petInfoData['id'] # 宠物ID
        pet_data_copy['pet_name'] = petInfoData['pet_name'] # 宠物名称
        pet_data_copy['category'] = petInfoData['kind'] # 宠物种类
        pet_data_copy['kind'] = petInfoData['species'] # 宠物品种
        pet_data_copy['gender'] = petInfoData['pet_sex'] # 宠物性别 0-未知 1-公 2-母
        pet_data_copy['birthday'] = petInfoData['pet_birthday'] # 宠物生日
        pet_data_copy['addday'] = petInfoData['add_time'] # 创建时间
        pet_data_copy['weight'] = petInfoData['weight'] # 体重
        pet_data_copy['sterilization'] = petInfoData['is_sterilized'] # 是否绝育 0-否 1-是 2-未知
        pet_data_copy['repellent'] = petInfoData['is_insecticide'] # 是否驱虫 0-否 1-是 2-未知
        pet_data_copy['vaccines'] = petInfoData['is_immunity'] # 是否免疫 0-否 1-是 2-未知
        pet_data_copy['is_dead'] = petInfoData['is_dead'] # 是否死亡 0-否 1-正常
        pet_data_copy['record_no'] = petInfoData['pet_code'] # 病历号
        pet_data_copy['pet_color'] = petInfoData['coat_color'] # 毛色
        pet_data_copy['hospital_id'] = petInfoData['hospital_id']
        pet_data_copy['hospital_code'] = petInfoData['hospital_code']
        pet_data_copy['hospital_name'] = petInfoData['hospital_name']


        csv_file = './医院数据/宠物数据.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file) and os.path.getsize(csv_file) > 0
        # 保存到.csv文件中
        with open(csv_file,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = pet_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerow(pet_data_copy)
    


    with open(f'./' + file_ + '/customer3.json','w',encoding='utf-8') as f:
        f.write(customerInfoResponse3.text)
    
    # 接口 4 响应体 （GET) http://127.0.0.1:13301/daily%2fwork%2fconsumer_tag%2f19  ------------------------------------------------------
    URL_4 = headURL + 'daily%2fwork%2fconsumer_tag%2f' + str(customer['id'])
    customerInfoResponse4 = requests.get(URL_4,headers=headers)
    with open(f'./' + file_ + '/customer4.json','w',encoding='utf-8') as f:
        f.write(customerInfoResponse4.text)



# 获取消费记录 （POST) http://127.0.0.1:13301/consumer%2fcenter%2fconsumption_record 
def getExpenseCalendarData(customer):
    URL_ex_ca_all = headURL + 'consumer%2fcenter%2fconsumption_record'
    data = {
        "pet_id": 0,
        "consumer_id": customer['id'],
        "bill_state": 0,
        "start": "2019-01-01",
        "end": "2025-01-01",
        "project_type": 0
    }
    response = requests.post(URL_ex_ca_all,data=json.dumps(data),headers=headers)

    file_ = '医院数据/消费记录/' + str(customer['id']) + '-' + replace_special_chars(customer['name'].strip())
    if not os.path.exists(file_):   # 不存在则创建
    # 创建文件夹
        os.makedirs(file_)

    with open(f'./' + file_ + '/expenseCalendar.json','w',encoding='utf-8') as f:
        f.write(response.text)
    
    # 遍历宠物编号获取订单号
    for pet in customer['pets']:
        # 根据 宠物编号获取 订单列表  (POST) http://127.0.0.1:13301/daily%2fwork%2fbill_list 
        URL_pet_code = headURL + 'daily%2fwork%2fbill_list'
        dataPetCode = {
            "start": "2019-01-02",
            "end": "2025-01-02",
            "key_word": pet['code'],
            "type": 9,
            "show_by_consumer_or_pet": 0
        }
        petOrderResponse = requests.post(URL_pet_code,data=json.dumps(dataPetCode),headers=headers)
        filePetCode = file_ + '/' + replace_special_chars(pet['name'].strip())
        if not os.path.exists(filePetCode):   # 不存在则创建
            # 创建文件夹
            os.makedirs(filePetCode)
        with open(f'./' + filePetCode + '/totalOrder.json','w',encoding='utf-8') as f:
            f.write(petOrderResponse.text)

        # 遍历订单 id 获取订单详细信息
        for order in json.loads(petOrderResponse.text)['Data']:
            # 根据 订单id 获取 详细订单信息  （POST）http://127.0.0.1:13301/daily%2fwork%2fbill_list_detail 
            URL_order_detail = headURL + 'daily%2fwork%2fbill_list_detail'
            dataorderDetail = {
                "id": order['id'],
                "bill_type": 1,
                "show_type": 0,
                "start": "",
                "end": "",
                "ids": ""
            }
            orderDetailResponse = requests.post(URL_order_detail, data=json.dumps(dataorderDetail), headers=headers)
            with open(f'./' + filePetCode + '/' + str(order['id']) + '-orderDetail.json','w',encoding='utf-8') as f:
                f.write(orderDetailResponse.text)


        
# 获取商品信息  
def getProductData(product_data):
    # 类目信息
    catalog_dict = {}
    # (GET) http://127.0.0.1:13301/base%2fsetting%2fusage
    product_detail_other1 = headURL + 'base%2fsetting%2fusage'
    # (GET) http://127.0.0.1:13301/base%2fsetting%2fuseunit
    product_detail_other2 = headURL + 'base%2fsetting%2fuseunit'
    # (GET) http://127.0.0.1:13301/base%2fsetting%2fkind
    product_detail_other3 = headURL + 'base%2fsetting%2fkind'
    product_detail_other1_response = requests.get(product_detail_other1,headers=headers)
    product_detail_other2_response = requests.get(product_detail_other2,headers=headers)
    product_detail_other3_response = requests.get(product_detail_other3,headers=headers)

    file_other = '医院数据/商品信息/'
    if not os.path.exists(file_other):   # 不存在则创建
        # 创建文件夹
        os.makedirs(file_other)
    
    # 将商品类目写入到 usage.json 中
    with open(f'./' + file_other + '/usage.json','w',encoding='utf-8') as f:
        f.write(product_detail_other1_response.text)
    # 将商品类目写入到 useunit.json 中
    with open(f'./' + file_other + '/useunit.json','w',encoding='utf-8') as f:
        f.write(product_detail_other2_response.text)
    # 将商品类目写入到 kind.json 中
    with open(f'./' + file_other + '/kind.json','w',encoding='utf-8') as f:
        f.write(product_detail_other3_response.text)
    



    # 获取商品类目  （GET）http://127.0.0.1:13301/base%2fsetting%2fcategory%2fsub%2f1  
    # 备注： 从 1-12分别为：挂号，处方，检验，影像，处置，手术，住院，寄养，疫苗，驱虫，美容，商品；非处方为71
    catalog_list = ['占位','挂号','处方','检验','影像','处置','手术','住院','寄养','疫苗','驱虫','美容','商品','非处方']
    URL_product = headURL + 'base%2fsetting%2fcategory%2fsub%2f'
    for i in range(1,14):
        product_list = []
        # print('正在采集商品信息：' + catalog_list[i] + '中！！！')
        if i == 13:
            URL_product_catalog = URL_product + '71'
        else:
            URL_product_catalog = URL_product + str(i)
        
        response = requests.get(URL_product_catalog,headers=headers)

        file_ = '医院数据/商品信息/' + catalog_list[i]
        if not os.path.exists(file_):   # 不存在则创建
            # 创建文件夹
            os.makedirs(file_)

        # 将商品类目写入到 catalog-list.json 中
        with open(f'./' + file_ + '/catalog-list.json','w',encoding='utf-8') as f:
            f.write(response.text)

        responseListData = json.loads(response.text)['Data']

        if responseListData == []: 
            continue

        data_all = []
        # 获取商品详细信息  （POST）http://127.0.0.1:13301/base%2fsetting%2fgoods%2fget
        URL_product_detail = headURL + 'base%2fsetting%2fgoods%2fget'
        for responseData in responseListData:
            print('正在采集商品信息：' + catalog_list[i] + '-' + responseData['name'] + '中！！！')
            # 记录所有的二级目录 id 映射 name
            catalog_dict[str(responseData['id'])] = responseData['name']
            # 记录所有的商品二级目录信息
            data_all.append(int(responseData['id']))
            data = int(responseData['id'])
            productResponse = requests.post(URL_product_detail,data=json.dumps(data),headers=headers)
            
            file_product = file_ + '/' + replace_special_chars(responseData['name'].strip())
            if not os.path.exists(file_product):   # 不存在则创建
                # 创建文件夹
                os.makedirs(file_product)
            # 将商品写入到 product.json 中
            with open(f'./' + file_product + '/product.json','w',encoding='utf-8') as f:
                f.write(productResponse.text)
        
        data_all_str = ','.join(map(str, data_all))
        responseListAll = requests.post(URL_product_detail,data=data_all_str,headers=headers_text)

        # 将所有商品写入到 product-all.json 中
        with open(f'./' + file_ + '/product-all.json','w',encoding='utf-8') as f:
            f.write(responseListAll.text)

        print('正在写入:' + catalog_list[i] + '-商品信息到CSV中！！！')

        # 组装数据到 product_list 中
        for product in json.loads(responseListAll.text)['Data']:
            # print(product)
            # print(replace_special_chars(catalog_dict[str(product['con_category_id'])].strip())) # 口服类

            # 更详细信息  （GET) http://127.0.0.1:13301/base%2fsetting%2fgood%2f1693
            URL_product_detail_other = headURL + 'base%2fsetting%2fgood%2f' + str(product['id'])
            product_detail_response = requests.get(URL_product_detail_other,headers=headers)
            file_product_other = file_ + '/' + replace_special_chars(catalog_dict[str(product['con_category_id'])].strip())
            if not os.path.exists(file_product_other):   # 不存在则创建
                # 创建文件夹
                os.makedirs(file_product_other)
            # 将所有商品写入到 product-[name].json 中
            with open(f'./' + file_product_other + '/product-' + replace_special_chars(product['name'].strip()) + '.json','w',encoding='utf-8') as f:
                f.write(product_detail_response.text)
            
            productDetailResponseData = json.loads(product_detail_response.text)['Data']

            product_data_copy = copy.deepcopy(product_data)  # 深拷贝，浅拷贝会出问题
            # task_id 老子不知道
            product_data_copy['goods_code'] = product['code'] # 商品编号
            product_data_copy['sale_state'] = product['on_and_off_shelves'] # 商品是否上下架  0-上架 1-下架
            product_data_copy['name'] = product['name'] # 商品名称
            # common_name 通用名 参数无
            # forshort 简称 参数无
            # print_name 打印名 参数无
            product_data_copy['spec'] = product['format'] # 规格
            product_data_copy['barcode'] = product['encode'] # 条码
            product_data_copy['category1'] = product['top_category_id'] # 一级类别
            product_data_copy['category2'] = product['con_category_id'] # 二级类别
            # category3 三级类别 无参数
            # category4 四级类别 无参数 
            product_data_copy['cost_price'] = product['buyprice'] # 成本价
            product_data_copy['sale_price'] = product['saleprice'] # 销售价
            product_data_copy['unit'] = product['unit'] # 单位
            product_data_copy['dosageunit'] = productDetailResponseData['useunit'] # 用量单位
            # allow_addcountcard 允许开卡 无参数
            product_data_copy['is_calculating_store'] = product['isuse_stock'] # 是否计算库存 0-否 1-是
            # safe_store 安全库存 无参数
            product_data_copy['use_method'] = product['usages'] # 给药途径
            # printlable 打印标签 无参数
            # drug_message 药品信息 无参数
            # drug_tips 药品Tips 无参数
            product_data_copy['manufacturer'] = product['vender'] # 生产厂商
            product_data_copy['brand_name'] = product['brand'] # 品牌名称
            # license_number 批准文号 无参数   
            product_data_copy['remark'] = product['guideline'] # 备注-说明
            # supplier 供应商 无参数
            # inspection_name 化验名称 无参数
            # inspection_brand 化验品牌名 无参数
            # inspection_model 化验厂商名 无参数
            # stock 库存 无参数

            product_list.append(product_data_copy)

        csv_file = './医院数据/商品信息.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file) and os.path.getsize(csv_file) > 0
        # 保存到.csv文件中
        with open(csv_file,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = product_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerows(product_list)
        











# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 获取商品信息
getProductData(product_data)



# ---------------------------------------------------------------------------------------------
# for customer in customer_data['Data']:

#     # user_head_CSV = ['task_id','owner_id','owner_name','owner_gender','owner_vip_level','owner_phone1','owner_phone2','owner_deposit','owner_integral','owner_address','owner_reg_date','owner_remarks','owner_source','sale_state','is_customer','hospital_id','hospital_code','hospital_name']
        
#     print('正在采集客户：' + str(customer['id']) + '-' + customer['name'] + ' 数据中！！！')

#     # 获取客户信息
#     getCustomerData(customer,user_data,pet_data,card_data)

#     # 获取消费记录
#     getExpenseCalendarData(customer)








print("数据导出完毕！！!")
os.system("pause")



