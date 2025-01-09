import requests
import json
import os
import csv
import re
import copy
import logging
import traceback

# 配置日志记录
logging.basicConfig(filename='yixin.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

""" try:
    print(a)
except Exception as e:
    logging.error(f"错误：{e}") """
    


info = input('请输入参数-info:')
sign = input('请输入参数-sign:')
userid = input('请输入参数-userId:')

# info = 'GBZa3ajLfh|VrAGvMjLwd'
# sign = '0005d5b1b4187661204abb15184604ad'
# userid = '1'

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

vaccine_data = {
    'task_id': '',
    'id': '',
    'createtime': '',
    'creater': '',
    'owner_id': '',
    'pet_id': '',
    'name': '',
    'hospital_id': '',
    'hospital_code': '',
    'hospital_name': ''
}

vaccine_detail_data = {
    'task_id': '',
    'createtime': '',
    'creater': '',
    'updater': '',
    'his_protection_id': '',
    'cure_employee_name': '',
    'name': '',
    'weight': '',
    'temperature': '',
    'discription': '',
    'eventtime': '',
    'state': '',
    'hospital_id': '',
    'hospital_code': '',
    'hospital_name': '',
    'add_employee_name': '',
    'con_category_name': '',
    'commodity_name': '',
    'commodity_brand': ''
}

product_catalog_data = {
    'task_id': '',
    'category_id': '',
    'parent_id': '',
    'category_name': ''
}

cases_data = {
    'task_id': '',
    'id': '',
    'createtime': '',
    'updatetime': '',
    'creater': '',
    'updater': '',
    'owner_id': '',
    'pet_id': '',
    'cure_employee_name': '',
    'live_id': '',
    '_code': '',
    'eventtime': '',
    'diagnosis': '',
    'abstract': '',
    'temperature': '',
    'weight': '',
    'breathe': '',
    'heartrate': '',
    'crt': '',
    'tongkong': '',
    'chiefnote': '',
    'checknote': '',
    'carenote': '',
    'processnote': '',
    'physicalorder': '',
    'conditionnote': '',
    'visitrecord': '',
    'hospitalnode': '',
    'sameclinic': '',
    'healthcheck': '',
    'service_employee_id': '',
    'service_employee_name': '',
    'file_description': '',
    'group_id': '',
    'state': '',
    'open_appointment': '',
    'appointment_time': '',
    'is_share': '',
    'blood_pressure': '',
    'surgical_record': '',
    'is_apply': '',
    'select_model': '',
    'whethertotransfer': '',
    'feeding_method': '',
    'feeding_frequency': '',
    'food_changes': '',
    'vaccine_status': '',
    'deworming_status': '',
    'previous_medical_records': '',
    'mentality': '',
    'mentality_other': '',
    'visible_mucosa': '',
    'physical_condition_score': '',
    'muscle_score': '',
    'periodontal_score': '',
    'heart_lung': '',
    'abdomen': '',
    'lymph_gland': '',
    'skin_elasticity': '',
    'eye_condition': '',
    'oral_mucosa': '',
    'suspected_illness': '',
    'eyes': '',
    'nose': '',
    'ears': '',
    'muscle': '',
    'skin': '',
    'nerve': '',
    'urology': '',
    'oral_cavity': '',
    'is_vaccine': '',
    'is_deworming': '',
    'clinical_examination': '',
    'case_level': '',
    'present_history': '',
    'is_tw': '',
    'evet_rft': ''
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

# 采集数据起止日期-结束日期
start_time = '2019-01-01'
end_time = '2027-01-01'

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

# 将顾客信息写入customer-all.json中
with open(f'./医院数据/customer-all.json','w',encoding='utf-8') as f:
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
    

    csv_file1 = './医院数据/用户数据.csv'
    # 检查文件是否存在且不为空
    file_exists = os.path.isfile(csv_file1) and os.path.getsize(csv_file1) > 0
    # 保存到.csv文件中
    with open(csv_file1,'a',encoding='utf-8',newline='') as f:
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
    if not isinstance(cardInfoDataList,list):
        cardInfoDataList = []

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


        csv_file2 = './医院数据/用户卡信息.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file2) and os.path.getsize(csv_file2) > 0
        # 保存到.csv文件中
        with open(csv_file2,'a',encoding='utf-8',newline='') as f:
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
    if not isinstance(petInfoDataList,list):
        petInfoDataList = []

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


        csv_file3 = './医院数据/宠物数据.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file3) and os.path.getsize(csv_file3) > 0
        # 保存到.csv文件中
        with open(csv_file3,'a',encoding='utf-8',newline='') as f:
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
        "start": start_time,
        "end": end_time,
        "project_type": 0
    }
    response = requests.post(URL_ex_ca_all,data=json.dumps(data),headers=headers)

    file_ = '医院数据/消费记录/' + str(customer['id']) + '-' + replace_special_chars(customer['name'].strip())
    if not os.path.exists(file_):   # 不存在则创建
    # 创建文件夹
        os.makedirs(file_)

    with open(f'./' + file_ + '/expense-calendar.json','w',encoding='utf-8') as f:
        f.write(response.text)

    responseData = json.loads(response.text)['Data']
    if not isinstance(responseData,list):
        responseData = []

    # 遍历消费记录表获取订单详情
    for order in responseData:
        # 根据 订单id 获取 详细订单信息  （POST）http://127.0.0.1:13301/daily%2fwork%2fbill_list_detail 
        URL_order_detail = headURL + 'daily%2fwork%2fbill_list_detail'

        dataorderDetail_0 = {
            "id": order['pet_id'],
            "bill_type": 0,
            "show_type": 0,
            "start": "",
            "end": "",
            "ids": ""
        }

        dataorderDetail_1 = {
            "id": order['id'],
            "bill_type": 1,
            "show_type": 0,
            "start": "",
            "end": "",
            "ids": ""
        }

        if int(order['id']) == 0:
            orderDetailResponse = requests.post(URL_order_detail, data=json.dumps(dataorderDetail_0), headers=headers)
        else:
            orderDetailResponse = requests.post(URL_order_detail, data=json.dumps(dataorderDetail_1), headers=headers)
        
        file_detail = file_ + '/' + str(order['pet_id']) + '-' + replace_special_chars(order['pet_name'].strip())
        if not os.path.exists(file_detail):   # 不存在则创建
        # 创建文件夹
            os.makedirs(file_detail)
        with open(f'./' + file_detail + '/' + str(order['id']) + '-orderDetail.json','w',encoding='utf-8') as f:
                f.write(orderDetailResponse.text)
            

        
# 获取商品信息  
def getProductData(product_data,product_catalog_data):
    # 类目列表
    product_catalog_data_list = []
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
        # 商品类目
        product_catalog_data_copy = copy.deepcopy(product_catalog_data) # 深拷贝

        product_list = []
        # print('正在采集商品信息：' + catalog_list[i] + '中！！！')
        if i == 13:
            URL_product_catalog = URL_product + '71'
        else:
            URL_product_catalog = URL_product + str(i)
        
        response = requests.get(URL_product_catalog,headers=headers)

        file_ = '医院数据/商品信息/' + str(i) + '-' + catalog_list[i]
        if not os.path.exists(file_):   # 不存在则创建
            # 创建文件夹
            os.makedirs(file_)

        # 将商品类目写入到 catalog-list.json 中
        with open(f'./' + file_ + '/catalog-list.json','w',encoding='utf-8') as f:
            f.write(response.text)

        responseListData = json.loads(response.text)['Data']
        if not isinstance(responseListData,list):
            responseListData = []

        if responseListData == []: 
            # task_id 老子不知道
            # category_id 分类ID 为空
            product_catalog_data_copy['parent_id'] = str(i) # 父类分类ID
            # category_name 分类名称 为空
            product_catalog_data_list.append(product_catalog_data_copy)
            continue
        
        data_all = []
        # 获取商品详细信息  （POST）http://127.0.0.1:13301/base%2fsetting%2fgoods%2fget
        URL_product_detail = headURL + 'base%2fsetting%2fgoods%2fget'

        for responseData in responseListData:
            # 商品类目
            product_catalog_data_copy = copy.deepcopy(product_catalog_data) # 深拷贝
            # task_id 老子不知道
            product_catalog_data_copy['category_id'] = responseData['id'] # 分类 id
            product_catalog_data_copy['parent_id'] = responseData['con_category_id'] # 父类分类ID
            product_catalog_data_copy['category_name'] = responseData['name'] # 分类名称
            product_catalog_data_list.append(product_catalog_data_copy)



            print('正在采集商品信息：' + catalog_list[i] + '-' + responseData['name'] + '中！！！')
            # 记录所有的二级目录 id 映射 name
            catalog_dict[str(responseData['id'])] = responseData['name']
            # 记录所有的商品二级目录信息
            data_all.append(int(responseData['id']))
            data = int(responseData['id'])
            productResponse = requests.post(URL_product_detail,data=json.dumps(data),headers=headers)
            
            file_product = file_ + '/' + str(responseData['id']) + '-' + replace_special_chars(responseData['name'].strip())
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

        responseListAllData = json.loads(responseListAll.text)['Data']

        if not isinstance(responseListAllData,list):
            responseListAllData = []

        # 组装数据到 product_list 中
        for product in responseListAllData:
            # print(product)
            # print(replace_special_chars(catalog_dict[str(product['con_category_id'])].strip())) # 口服类

            # 更详细信息  （GET) http://127.0.0.1:13301/base%2fsetting%2fgood%2f1693
            URL_product_detail_other = headURL + 'base%2fsetting%2fgood%2f' + str(product['id'])
            product_detail_response = requests.get(URL_product_detail_other,headers=headers)
            file_product_other = file_ + '/' + str(product['con_category_id']) +  '-' + replace_special_chars(catalog_dict[str(product['con_category_id'])].strip())
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

        csv_file4 = './医院数据/商品信息.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file4) and os.path.getsize(csv_file4) > 0
        # 保存到.csv文件中
        with open(csv_file4,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = product_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerows(product_list)
        
    csv_file5 = './医院数据/商品分类信息.csv'
    # 检查文件是否存在且不为空
    file_exists = os.path.isfile(csv_file5) and os.path.getsize(csv_file5) > 0
    # 保存到.csv文件中
    with open(csv_file5,'a',encoding='utf-8',newline='') as f:
        # 将文件对象转换成 DictWriter 对象
        writer = csv.DictWriter(f,fieldnames = product_catalog_data.keys())
        # 如果文件是新创建的，写入表头
        if not file_exists:
            writer.writeheader()
        writer.writerows(product_catalog_data_list)
        



# 获取疫苗驱虫信息  （POST）http://127.0.0.1:13301/consumer%2fcenter%2fvaccine_insect_record
def getVaccineData(customer,vaccine_data,vaccine_detail_data):

    # 客户信息 取医院编号  (GET) http://127.0.0.1:13301/daily%2fwork%2fconsumer%2f4497
    URL_customer = headURL + 'daily%2fwork%2fconsumer%2f' + str(customer['id'])
    customer_response = requests.get(URL_customer,headers=headers)
    customerResponseData = json.loads(customer_response.text)['Data']

    # 客户疫苗免疫信息（POST）http://127.0.0.1:13301/consumer%2fcenter%2fvaccine_insect_record
    URL_Vaccine = headURL + 'consumer%2fcenter%2fvaccine_insect_record'
    data = {
        "pet_id": 0,
        "consumer_id": customer['id'],
        "bill_state": 0,
        "start": start_time,
        "end": end_time,
        "project_type": 0
    }

    vaccine_response = requests.post(URL_Vaccine,data=json.dumps(data),headers=headers)

    vaccineResponseListData = json.loads(vaccine_response.text)['Data']
    if not isinstance(vaccineResponseListData,list):
        vaccineResponseListData = []

    # 组装数据到 vaccine_data 中
    for vaccineResponseData in vaccineResponseListData:
        vaccine_data_copy = copy.deepcopy(vaccine_data) # 深拷贝
        # task_id 老子不知道
        vaccine_data_copy['id'] = vaccineResponseData['id'] # 疫苗单ID
        vaccine_data_copy['createtime'] = vaccineResponseData['event_time'] # 数据添加时间
        vaccine_data_copy['creater'] = vaccineResponseData['cure_employee_name'] # 创建数据的人员名称
        vaccine_data_copy['owner_id'] = customer['id'] # 顾客ID
        vaccine_data_copy['pet_id'] = vaccineResponseData['pet_id'] # 宠物ID
        vaccine_data_copy['name'] = vaccineResponseData['protection_name'] + '-' + vaccineResponseData['protection_detail_name']+ '-' + vaccineResponseData['medication_content'] # 名称
        vaccine_data_copy['hospital_id'] = vaccineResponseData['hospital_id'] # 医院ID
        vaccine_data_copy['hospital_code'] = customerResponseData['hospital_code'] # 医院编号
        vaccine_data_copy['hospital_name'] = vaccineResponseData['hospital_name'] # 医院名称

        csv_file6 = './医院数据/疫苗单表.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file6) and os.path.getsize(csv_file6) > 0
        # 保存到.csv文件中
        with open(csv_file6,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = vaccine_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerow(vaccine_data_copy)



    file_ = '医院数据/免疫驱虫/' + str(customer['id']) + '-' + replace_special_chars(customer['name'].strip())
    if not os.path.exists(file_):   # 不存在则创建
        # 创建文件夹
        os.makedirs(file_)

    # 将免疫驱虫信息写入vaccine-all.json中
    with open(f'./' + file_ + '/vaccine-all.json','w',encoding='utf-8') as f:
        f.write(vaccine_response.text)
    
    # 使用顾客 ID 查找宠物信息  (GET)  http://127.0.0.1:13301/daily%2fwork%2fpets%2f529
    URL_pets = headURL + 'daily%2fwork%2fpets%2f' + str(customer['id'])
    pets_response = requests.get(URL_pets,headers=headers)

    petsResponseData = json.loads(pets_response.text)['Data']

    if not isinstance(petsResponseData, list):
        petsResponseData = []

    for pet in petsResponseData:
        # 疫苗头部信息  (GET) http://127.0.0.1:13301/daily%2fwork%2fclinic_pet%2f601 
        URL_clinic_pet = headURL + 'daily%2fwork%2fclinic_pet%2f' + str(pet['id'])
        clinic_pet_response = requests.get(URL_clinic_pet,headers=headers)
        clinicPetResponseData = json.loads(clinic_pet_response.text)['Data']
        file_pet = file_ + '/' + str(pet['id']) + '-' + replace_special_chars(pet['pet_name'].strip())
        if not os.path.exists(file_pet):   # 不存在则创建
        # 创建文件夹
            os.makedirs(file_pet)
        # 将疫苗头部信息 写入vaccine-head.json中
        with open(f'./' + file_pet + '/vaccine-head.json','w',encoding='utf-8') as f:
            f.write(clinic_pet_response.text)


        # 疫苗导航栏信息  （GET）http://127.0.0.1:13301/daily%2fwork%2fprotections%2f601 
        URL_protections = headURL + 'daily%2fwork%2fprotections%2f' + str(pet['id'])
        protections_response = requests.get(URL_protections,headers=headers)
        # 将疫苗导航栏信息 写入vaccine-nav.json中
        with open(f'./' + file_pet + '/vaccine-nav.json','w',encoding='utf-8') as f:
            f.write(protections_response.text)

        protectionsResponseListData = json.loads(protections_response.text)['Data']
        if not isinstance(protectionsResponseListData,list):
            protectionsResponseListData = []
        for protection in protectionsResponseListData: 
            # 疫苗详细信息（GET）http://127.0.0.1:13301/daily%2fwork%2fprotection%2f115%2f529 
            URL_protection = headURL + 'daily%2fwork%2fprotection%2f' + str(protection['id']) + '%2f' + str(customer['id'])
            protection_response = requests.get(URL_protection,headers=headers)
            # 将疫苗详细信息 写入 protection['id']-protection['name']
            with open(f'./' + file_pet + '/' + str(protection['id']) + '-' + protection['name'] +  '.json','w',encoding='utf-8') as f:
                f.write(protection_response.text)
            
            protectionResponseData = json.loads(protection_response.text)['Data']
            if not isinstance(protectionResponseData,list):
                protectionResponseData = []
            
            for protectionData in protectionResponseData:
                # 组装数据到 vaccine_detail_data 中
                vaccine_detail_data_copy = copy.deepcopy(vaccine_detail_data) # 深拷贝
                # task_id 老子不知道
                vaccine_detail_data_copy['createtime'] = protectionData['eventtime'] # 数据添加时间
                vaccine_detail_data_copy['creater'] = protectionData['cure_employee_name'] # 添加信息人员
                # updater 最后修改信息人员 参数无
                vaccine_detail_data_copy['his_protection_id'] = protectionData['his_protection_id'] # 疫苗单ID
                vaccine_detail_data_copy['cure_employee_name'] = protectionData['cure_employee_name'] # 主治医生
                vaccine_detail_data_copy['name'] = protectionData['name'] # 名称
                vaccine_detail_data_copy['weight'] = protectionData['weight'] # 体重
                vaccine_detail_data_copy['temperature'] = protectionData['temperature'] # 体温
                vaccine_detail_data_copy['discription'] = protectionData['discription'] # 备注
                vaccine_detail_data_copy['eventtime'] = protectionData['eventtime'] # 疫苗时间
                vaccine_detail_data_copy['state'] = protectionData['state'] # 免疫驱虫状态 0-未完成  1-已完成
                vaccine_detail_data_copy['hospital_id'] = clinicPetResponseData['hospital_id'] # 医院ID
                vaccine_detail_data_copy['hospital_code'] = clinicPetResponseData['hospital_code'] # 医院编号
                vaccine_detail_data_copy['hospital_name'] = clinicPetResponseData['hospital_name'] # 医院名称
                if isinstance(protectionData['his_consumptions'],list):
                    for hisConsumptions in protectionData['his_consumptions']:
                        vaccine_detail_data_copy['add_employee_name'] = hisConsumptions['add_employee_name'] # 付医生
                        vaccine_detail_data_copy['con_category_name'] = hisConsumptions['con_category_name'] # 疫苗服务
                        vaccine_detail_data_copy['commodity_name'] = hisConsumptions['commodity_name'] # 妙三多
                        vaccine_detail_data_copy['commodity_brand'] = hisConsumptions['commodity_brand'] # 硕腾

                        csv_file7 = './医院数据/疫苗单详情表.csv'
                        # 检查文件是否存在且不为空
                        file_exists = os.path.isfile(csv_file7) and os.path.getsize(csv_file7) > 0
                        # 保存到.csv文件中
                        with open(csv_file7,'a',encoding='utf-8',newline='') as f:
                            # 将文件对象转换成 DictWriter 对象
                            writer = csv.DictWriter(f,fieldnames = vaccine_detail_data.keys())
                            # 如果文件是新创建的，写入表头
                            if not file_exists:
                                writer.writeheader()
                            writer.writerow(vaccine_detail_data_copy)
                else:
                    csv_file7 = './医院数据/疫苗单详情表.csv'
                    # 检查文件是否存在且不为空
                    file_exists = os.path.isfile(csv_file7) and os.path.getsize(csv_file7) > 0
                    # 保存到.csv文件中
                    with open(csv_file7,'a',encoding='utf-8',newline='') as f:
                        # 将文件对象转换成 DictWriter 对象
                        writer = csv.DictWriter(f,fieldnames = vaccine_detail_data.keys())
                        # 如果文件是新创建的，写入表头
                        if not file_exists:
                            writer.writeheader()
                        writer.writerow(vaccine_detail_data_copy)

            
        
        # 驱虫导航栏信息  (GET) http://127.0.0.1:13301/daily%2fwork%2finsects%2f601 
        URL_insects = headURL + 'daily%2fwork%2finsects%2f' + str(pet['id'])
        insects_response = requests.get(URL_insects,headers=headers)

        # 将驱虫导航栏信息 写入insecticide-nav.json中
        with open(f'./' + file_pet + '/insecticide-nav.json','w',encoding='utf-8') as f:
            f.write(insects_response.text)
        
        insectsResponseListData = json.loads(insects_response.text)['Data']
        if not isinstance(insectsResponseListData,list):
            insectsResponseListData = []
        for insect in insectsResponseListData:
            # 驱虫详细信息  (GET) http://127.0.0.1:13301/daily%2fwork%2finsect%2f43%2f529 
            URL_insect = headURL + 'daily%2fwork%2finsect%2f' + str(insect['id']) + '%2f' + str(customer['id'])
            insect_response = requests.get(URL_insect,headers=headers)
            # 将驱虫详细信息 写入 insect['id']-insect['name']
            with open(f'./' + file_pet + '/' + str(insect['id']) + '-' + insect['name'] +  '.json','w',encoding='utf-8') as f:
                f.write(insect_response.text)

            insectResponseData = json.loads(insect_response.text)['Data']
            if not isinstance(insectResponseData,list):
                insectResponseData = []

            for insectData in insectResponseData:
                # 组装数据到 vaccine_detail_data 中
                vaccine_detail_data_copy = copy.deepcopy(vaccine_detail_data) # 深拷贝
                # task_id 老子不知道
                vaccine_detail_data_copy['createtime'] = insectData['eventtime'] # 数据添加时间
                vaccine_detail_data_copy['creater'] = insectData['cure_employee_name'] # 添加信息人员
                # updater 最后修改信息人员ID 参数无
                vaccine_detail_data_copy['his_protection_id'] = insectData['id'] # 疫苗单ID
                vaccine_detail_data_copy['cure_employee_name'] = insectData['cure_employee_name'] # 主治医生
                vaccine_detail_data_copy['name'] = insectData['name'] # 名称
                vaccine_detail_data_copy['weight'] = insectData['weight'] # 体重
                vaccine_detail_data_copy['temperature'] = insectData['temperature'] # 体温
                vaccine_detail_data_copy['discription'] = insectData['discription'] # 备注
                vaccine_detail_data_copy['eventtime'] = insectData['eventtime'] # 疫苗时间
                vaccine_detail_data_copy['state'] = insectData['state'] # 免疫驱虫状态 0-未完成  1-已完成
                vaccine_detail_data_copy['hospital_id'] = clinicPetResponseData['hospital_id'] # 医院ID
                vaccine_detail_data_copy['hospital_code'] = clinicPetResponseData['hospital_code'] # 医院编号
                vaccine_detail_data_copy['hospital_name'] = clinicPetResponseData['hospital_name'] # 医院名称
                if isinstance(insectData['his_consumptions'],list):
                    for hisConsumptions in insectData['his_consumptions']:
                        vaccine_detail_data_copy['add_employee_name'] = hisConsumptions['add_employee_name'] # 付医生
                        vaccine_detail_data_copy['con_category_name'] = hisConsumptions['con_category_name'] # 疫苗服务
                        vaccine_detail_data_copy['commodity_name'] = hisConsumptions['commodity_name'] # 妙三多
                        vaccine_detail_data_copy['commodity_brand'] = hisConsumptions['commodity_brand'] # 硕腾

                        csv_file7 = './医院数据/疫苗单详情表.csv'
                        # 检查文件是否存在且不为空
                        file_exists = os.path.isfile(csv_file7) and os.path.getsize(csv_file7) > 0
                        # 保存到.csv文件中
                        with open(csv_file7,'a',encoding='utf-8',newline='') as f:
                            # 将文件对象转换成 DictWriter 对象
                            writer = csv.DictWriter(f,fieldnames = vaccine_detail_data.keys())
                            # 如果文件是新创建的，写入表头
                            if not file_exists:
                                writer.writeheader()
                            writer.writerow(vaccine_detail_data_copy)
                else:
                    csv_file7 = './医院数据/疫苗单详情表.csv'
                    # 检查文件是否存在且不为空
                    file_exists = os.path.isfile(csv_file7) and os.path.getsize(csv_file7) > 0
                    # 保存到.csv文件中
                    with open(csv_file7,'a',encoding='utf-8',newline='') as f:
                        # 将文件对象转换成 DictWriter 对象
                        writer = csv.DictWriter(f,fieldnames = vaccine_detail_data.keys())
                        # 如果文件是新创建的，写入表头
                        if not file_exists:
                            writer.writeheader()
                        writer.writerow(vaccine_detail_data_copy)

        


# 获取病例信息  （POST) http://127.0.0.1:13301/consumer%2fcenter%2fmedical_record
def getCasesData(customer,cases_data):
    # 病例卡片信息 （POST) http://127.0.0.1:13301/consumer%2fcenter%2fmedical_record
    URL_medical_record = headURL + 'consumer%2fcenter%2fmedical_record'
    # 住院卡片信息  (POST) http://127.0.0.1:13301/consumer%2fcenter%2fhospitalization_record
    URL_hospitalization_record = headURL + 'consumer%2fcenter%2fhospitalization_record'
    data ={
        "pet_id": 0,
        "consumer_id": customer['id'],
        "bill_state": 0,
        "start": start_time,
        "end": end_time,
        "project_type": 0
    }
    medical_record_response = requests.post(URL_medical_record,data=json.dumps(data),headers=headers)
    hospitalization_record_response = requests.post(URL_hospitalization_record,data=json.dumps(data),headers=headers)
    medicalRecordResponseData = json.loads(medical_record_response.text)['Data']
    hospitalizationRecordResponseData = json.loads(hospitalization_record_response.text)['Data']

    
    file_ = '医院数据/病例信息/' + str(customer['id']) + '-' + replace_special_chars(customer['name'].strip())
    if not os.path.exists(file_):   # 不存在则创建
        # 创建文件夹
        os.makedirs(file_)

    # 将病例信息写入cases-all.json中
    with open(f'./' + file_ + '/cases-all.json','w',encoding='utf-8') as f:
        f.write(medical_record_response.text)
    # 将住院信息信息写入hospitalization-all.json中
    with open(f'./' + file_ + '/hospitalization-all.json','w',encoding='utf-8') as f:
        f.write(hospitalization_record_response.text)

    # 医疗记录版本信息  (GET)  http://127.0.0.1:13301/daily%2fwork%2fmedical_record_version 
    URL_medical_record_version = headURL + 'daily%2fwork%2fmedical_record_version'
    # 诊断信息 (GET) http://127.0.0.1:13301/daily%2fwork%2fdiagnosis
    URL_diagnosis = headURL + 'daily%2fwork%2fdiagnosis'
    # 给药途径 (GET) http://127.0.0.1:13301/base%2fsetting%2fusage
    URL_usage = headURL + 'base%2fsetting%2fusage'
    # {"Code":0,"Message":"SUCCESS","Data":["内科","外科"]} (GET) http://127.0.0.1:13301/daily%2fwork%2fabstracts
    URL_abstracts = headURL + 'daily%2fwork%2fabstracts'

    medical_record_version_response = requests.get(URL_medical_record_version,headers=headers)
    diagnosis_response = requests.get(URL_diagnosis,headers=headers)
    usage_response = requests.get(URL_usage,headers=headers)
    abstracts_response = requests.get(URL_abstracts,headers=headers)

    # 将医疗记录版本信息写入medical-record-version.json中
    with open(f'./' + file_ + '/medical-record-version.json','w',encoding='utf-8') as f:
        f.write(medical_record_version_response.text)
    # 将诊断信息写入diagnosis.json中
    with open(f'./' + file_ + '/diagnosis.json','w',encoding='utf-8') as f:
        f.write(diagnosis_response.text)
    # 将给药途径写入usage.json中
    with open(f'./' + file_ + '/usage.json','w',encoding='utf-8') as f:
        f.write(usage_response.text)
    # 将"Data":["内科","外科"]写入abstracts.json中
    with open(f'./' + file_ + '/abstracts.json','w',encoding='utf-8') as f:
        f.write(abstracts_response.text)



    if not isinstance(medicalRecordResponseData,list):
        medicalRecordResponseData = []

    # 获取病例详细信息
    for medicalRecordData in medicalRecordResponseData:
        # 病例详情头信息  (GET) http://127.0.0.1:13301/daily%2fwork%2fclinic_pet%2f160
        URL_cases_head = headURL + 'daily%2fwork%2fclinic_pet%2f' + str(medicalRecordData['pet_id'])
        # 病例导航信息  (GET) http://127.0.0.1:13301/daily%2fwork%2fmedical_record%2f160
        URL_cases_nav = headURL + 'daily%2fwork%2fmedical_record%2f' + str(medicalRecordData['pet_id'])
        # 回访名单信息  (GET) http://127.0.0.1:13301/daily%2fwork%2freturn_visit_list%2f234 
        URL_return_visit_list = headURL + 'daily%2fwork%2freturn_visit_list%2f' + str(medicalRecordData['id'])
        # 病例详情信息  (GET) http://127.0.0.1:13301/daily%2fwork%2fmedical_record_detail%2f234
        URL_cases_detail = headURL + 'daily%2fwork%2fmedical_record_detail%2f' + str(medicalRecordData['id'])
        

        cases_head_response = requests.get(URL_cases_head,headers=headers)
        cases_nav_response = requests.get(URL_cases_nav,headers=headers)
        return_visit_list_response = requests.get(URL_return_visit_list,headers=headers)
        cases_detail_response = requests.get(URL_cases_detail,headers=headers)

        file_detail = file_ + '/' + str(medicalRecordData['pet_id']) + '-' + replace_special_chars(medicalRecordData['pet_name'].strip()) + '/' + '病例'
        if not os.path.exists(file_detail):   # 不存在则创建
            # 创建文件夹
            os.makedirs(file_detail)
        
        # 将病详情头信息写入cases-head.json中
        with open(f'./' + file_detail + '/cases-head.json','w',encoding='utf-8') as f:
            f.write(cases_head_response.text)
        # 将病例导航信息写入cases-nav.json中
        with open(f'./' + file_detail + '/cases-nav.json','w',encoding='utf-8') as f:
            f.write(cases_nav_response.text)
        # 将回访名单信息写入['病例号']-return-visit-list.json中
        with open(f'./' + file_detail + '/' + str(medicalRecordData['id']) + '-' + 'return-visit-list.json','w',encoding='utf-8') as f:
            f.write(return_visit_list_response.text)
        # 将病例详情信息写入['病例号']-cases-detail.json中
        with open(f'./' + file_detail + '/' + str(medicalRecordData['id']) + '-' + 'cases-detail.json','w',encoding='utf-8') as f:
            f.write(cases_detail_response.text)
        
        # 组装数据到 cases_data 中
        casesDetailData = json.loads(cases_detail_response.text)['Data']
        cases_data_copy = copy.deepcopy(cases_data)
        # task_id 老子不知道
        cases_data_copy['id'] = casesDetailData['id'] # 病例ID
        cases_data_copy['createtime'] = casesDetailData['eventtime'] # 数据添加时间
        # updatetime 数据修改时间 参数无
        cases_data_copy['creater'] = casesDetailData['cure_employee_id'] # 添加人员ID
        # updater 最后修改信息人员ID 参数无
        cases_data_copy['owner_id'] = casesDetailData['his_consumer_id'] # 顾客ID
        cases_data_copy['pet_id'] = casesDetailData['his_pet_id'] # 宠物ID
        cases_data_copy['cure_employee_name'] = casesDetailData['cure_employee_name'] # 主治医生
        # live_id 住院ID 参数无
        cases_data_copy['_code'] = casesDetailData['code'] # 病例编号
        cases_data_copy['eventtime'] = casesDetailData['eventtime'] # 病例日期
        cases_data_copy['diagnosis'] = casesDetailData['diagnosis'] # 诊疗科目
        cases_data_copy['abstract'] = casesDetailData['abstract'] # 病症分类
        cases_data_copy['temperature'] = casesDetailData['temperature'] # 体温
        cases_data_copy['weight'] = casesDetailData['weight'] # 体重
        cases_data_copy['breathe'] = casesDetailData['breathe'] # 呼吸
        cases_data_copy['heartrate'] = casesDetailData['heartrate'] # 心率
        cases_data_copy['crt'] = casesDetailData['crt'] # crt
        cases_data_copy['tongkong'] = casesDetailData['tongkong'] # 瞳孔
        cases_data_copy['chiefnote'] = casesDetailData['chiefnote'] # 主诉记录
        cases_data_copy['checknote'] = casesDetailData['checknote'] # 检验分析
        cases_data_copy['carenote'] = casesDetailData['carenote'] # 护理记录
        cases_data_copy['processnote'] = casesDetailData['processnote'] # 处理治疗
        cases_data_copy['physicalorder'] = casesDetailData['physicalorder'] # 医嘱
        cases_data_copy['conditionnote'] = casesDetailData['conditionnote'] # 病情诊断
        cases_data_copy['visitrecord'] = casesDetailData['visitrecord'] # 回访记录
        cases_data_copy['hospitalnode'] = casesDetailData['hospitalnode'] # 住院病情
        cases_data_copy['sameclinic'] = casesDetailData['sameclinic'] # 疑似病例
        cases_data_copy['healthcheck'] = json.dumps(casesDetailData['healthcheck']) # 体格检查内容
        cases_data_copy['service_employee_id'] = casesDetailData['service_employee_id'] # 服务人员ID
        cases_data_copy['service_employee_name'] = casesDetailData['service_employee_name'] # 服务人员名称
        cases_data_copy['file_description'] = casesDetailData['file_description'] # 附件描述
        cases_data_copy['group_id'] = casesDetailData['group_id'] # 病例组ID
        cases_data_copy['state'] = casesDetailData['state'] # 病例状态
        cases_data_copy['open_appointment'] = casesDetailData['open_appointment'] # 是否开启预约
        cases_data_copy['appointment_time'] = casesDetailData['appointment_time'] # 预约时间
        cases_data_copy['is_share'] = casesDetailData['is_share'] # 是否和小程序共享查看病例
        cases_data_copy['blood_pressure'] = casesDetailData['blood_pressure'] # 血压
        cases_data_copy['surgical_record'] = casesDetailData['surgical_record'] # 手术记录
        cases_data_copy['is_apply'] = casesDetailData['is_apply'] # 申请/未申请
        # select_model 创建来源病历进行程（主诉、体况检查、检验分析、诊断治疗、医嘱/回访）字段无法匹配
        # whethertotransfer 是否为转过来的病历 无参数
        cases_data_copy['feeding_method'] = json.dumps(casesDetailData['feeding_method']) # 喂养方式
        cases_data_copy['feeding_frequency'] = casesDetailData['feeding_frequency'] # 喂养频次
        cases_data_copy['food_changes'] = casesDetailData['food_changes'] # 食物改变
        cases_data_copy['vaccine_status'] = json.dumps(casesDetailData['vaccine_status']) # 疫苗状态
        cases_data_copy['deworming_status'] = json.dumps(casesDetailData['deworming_status']) # 驱虫状态
        cases_data_copy['previous_medical_records'] = casesDetailData['previous_medical_records'] # 既往病例
        cases_data_copy['mentality'] = casesDetailData['mentality'] # 精神状态
        cases_data_copy['mentality_other'] = casesDetailData['mentality_other'] # 精神状态其他
        cases_data_copy['visible_mucosa'] = json.dumps(casesDetailData['visible_mucosa']) # 可视黏膜
        cases_data_copy['physical_condition_score'] = casesDetailData['physical_condition_score'] # 体况评分
        cases_data_copy['muscle_score'] = casesDetailData['muscle_score'] # 肌肉评分
        cases_data_copy['periodontal_score'] = casesDetailData['periodontal_score'] # 牙周评分
        cases_data_copy['heart_lung'] = json.dumps(casesDetailData['heart_lung']) # 心肺听诊
        cases_data_copy['abdomen'] = json.dumps(casesDetailData['abdomen']) # 腹部触诊
        cases_data_copy['lymph_gland'] = json.dumps(casesDetailData['lymph_gland']) # 淋巴结触诊
        cases_data_copy['skin_elasticity'] = casesDetailData['skin_elasticity'] # 皮肤弹性
        cases_data_copy['eye_condition'] = casesDetailData['eye_condition'] # 眼睛情况
        cases_data_copy['oral_mucosa'] = casesDetailData['oral_mucosa'] # 口腔粘膜
        cases_data_copy['suspected_illness'] = casesDetailData['suspected_illness'] # 疑似病症
        cases_data_copy['eyes'] = casesDetailData['eyes'] # 眼睛
        cases_data_copy['nose'] = casesDetailData['nose'] # 鼻部
        cases_data_copy['ears'] = casesDetailData['ears'] # 耳朵
        cases_data_copy['muscle'] = casesDetailData['muscle'] # 肌肉
        cases_data_copy['skin'] = casesDetailData['skins'] # 皮肤
        cases_data_copy['nerve'] = casesDetailData['nerve'] # 神经
        cases_data_copy['urology'] = casesDetailData['urology'] # 泌尿
        cases_data_copy['oral_cavity'] = casesDetailData['oral_cavity'] # 口腔
        cases_data_copy['is_vaccine'] = casesDetailData['is_vaccine'] # 未选/未/已经
        cases_data_copy['is_deworming'] = casesDetailData['is_deworming'] # 未选/未/已经
        cases_data_copy['clinical_examination'] = casesDetailData['clinical_examination'] # 临床检查
        cases_data_copy['case_level'] = casesDetailData['case_level'] # -
        cases_data_copy['present_history'] = casesDetailData['present_history'] # -
        try: # -
            cases_data_copy['is_tw'] = hospitalizationDetailData['is_tw']
        except Exception:
            cases_data_copy['is_tw'] = 0
        try: # rft
            cases_data_copy['evet_rft'] = hospitalizationDetailData['evet_rft']
        except Exception:
            cases_data_copy['evet_rft'] = ''

        csv_file8 = './医院数据/病例信息.csv'
        # 检查文件是否存在且不为空
        file_exists = os.path.isfile(csv_file8) and os.path.getsize(csv_file8) > 0
        # 保存到.csv文件中
        with open(csv_file8,'a',encoding='utf-8',newline='') as f:
            # 将文件对象转换成 DictWriter 对象
            writer = csv.DictWriter(f,fieldnames = cases_data.keys())
            # 如果文件是新创建的，写入表头
            if not file_exists:
                writer.writeheader()
            writer.writerow(cases_data_copy)
        

        
    if not isinstance(hospitalizationRecordResponseData,list):
        hospitalizationRecordResponseData = []
    # 获取住院详细信息
    for hospitalizationRecordData in hospitalizationRecordResponseData:
        # 住院详情头信息  (GET) http: //127.0.0.1:13301/daily%2fwork%2fclinic_pet%2f2299
        URL_hospitalization_head = headURL + 'daily%2fwork%2fclinic_pet%2f' + str(hospitalizationRecordData['pet_id'])
        # 住院导航信息    (GET) http://127.0.0.1:13301/daily%2fwork%2fhospitalizations%2f2299 
        URL_hospitalization_nav = headURL + 'daily%2fwork%2fhospitalizations%2f' + str(hospitalizationRecordData['pet_id'])
        # 住院表头信息    (GET) http://127.0.0.1:13301/daily%2fwork%2fhospitalization%2f697
        URL_hospitalization_table_head = headURL + 'daily%2fwork%2fhospitalization%2f' + str(hospitalizationRecordData['id'])

        hospitalization_head_response = requests.get(URL_hospitalization_head,headers=headers)
        hospitalization_nav_response = requests.get(URL_hospitalization_nav,headers=headers)
        hospitalization_table_head_response = requests.get(URL_hospitalization_table_head,headers=headers)

        file_detail = file_ + '/' + str(hospitalizationRecordData['pet_id']) + '-' + replace_special_chars(hospitalizationRecordData['pet_name'].strip()) + '/' + '住院'
        if not os.path.exists(file_detail):   # 不存在则创建
            # 创建文件夹
            os.makedirs(file_detail)
        # 将住院详情头信息写入hospitalization-head.json中
        with open(f'./' + file_detail + '/hospitalization-head.json','w',encoding='utf-8') as f:
            f.write(hospitalization_head_response.text)
        # 将住院导航信息写入hospitalization-nav.json中
        with open(f'./' + file_detail + '/hospitalization-nav.json','w',encoding='utf-8') as f:
            f.write(hospitalization_nav_response.text)
        # 将住院表头信息写入hospitalization-table-head.json中
        with open(f'./' + file_detail + '/hospitalization-table-head.json','w',encoding='utf-8') as f:
            f.write(hospitalization_table_head_response.text)


        hospitalizationNavResponseData = json.loads(hospitalization_nav_response.text)['Data']

        if not isinstance(hospitalizationNavResponseData,list):
            hospitalizationNavResponseData = []
        
        # 获取住院详细信息
        for hospitalizationNavData in hospitalizationNavResponseData:
            for clinic in hospitalizationNavData['clinics']:
                '''时间有问题'''
                # 住院时间信息  (GET) http://127.0.0.1:13301/consumer%2fcenter%2fmr_update_time%2f11247
                URL_hospitalization_time = headURL + 'consumer%2fcenter%2fmr_update_time%2f' + str(clinic['id'])
                # 回访名单信息  (GET)  http://127.0.0.1:13301/daily%2fwork%2freturn_visit_list%2f11247
                URL_hospitalization_return_visit_list = headURL + 'daily%2fwork%2freturn_visit_list%2f' + str(clinic['id'])
                # 住院详细信息  (GET) http: //127.0.0.1:13301/daily%2fwork%2fmedical_record_detail%2f11294
                URL_hospitalization_detail = headURL + 'daily%2fwork%2fmedical_record_detail%2f' + str(clinic['id'])

                hospitalization_time_response = requests.get(URL_hospitalization_time,headers=headers)
                hospitalization_return_visit_list_response = requests.get(URL_hospitalization_return_visit_list,headers=headers)
                hospitalization_detail_response = requests.get(URL_hospitalization_detail,headers=headers)
                
                # 将住院时间信息写入['住院号']-hospitalization-time.json中
                with open(f'./' + file_detail + '/' + str(clinic['id']) + '-' + 'hospitalization-time.json','w',encoding='utf-8') as f:
                    f.write(hospitalization_time_response.text)
                # 将回访名单信息写入['住院号']-hospitalization-return-visit-list.json中
                with open(f'./' + file_detail + '/' + str(clinic['id']) + '-' + 'hospitalization-return-visit-list.json','w',encoding='utf-8') as f:
                    f.write(hospitalization_return_visit_list_response.text)
                # 将住院详情信息写入['住院号']-hospitalization-detail.json中
                with open(f'./' + file_detail + '/' + str(clinic['id']) + '-' + 'hospitalization-detail.json','w',encoding='utf-8') as f:
                    f.write(hospitalization_detail_response.text)
                

                # 组装数据到 cases_data 中
                hospitalizationDetailData = json.loads(hospitalization_detail_response.text)['Data']
                cases_data_copy = copy.deepcopy(cases_data)
                # task_id 老子不知道
                cases_data_copy['id'] = hospitalizationDetailData['id'] # 病例ID
                cases_data_copy['createtime'] = hospitalizationDetailData['eventtime'] # 数据添加时间
                # updatetime 数据修改时间 参数无
                cases_data_copy['creater'] = hospitalizationDetailData['cure_employee_id'] # 添加人员ID
                # updater 最后修改信息人员ID 参数无
                cases_data_copy['owner_id'] = hospitalizationDetailData['his_consumer_id'] # 顾客ID
                cases_data_copy['pet_id'] = hospitalizationDetailData['his_pet_id'] # 宠物ID
                cases_data_copy['cure_employee_name'] = hospitalizationDetailData['cure_employee_name'] # 主治医生
                # live_id 住院ID 参数无
                cases_data_copy['_code'] = hospitalizationDetailData['code'] # 病例编号
                cases_data_copy['eventtime'] = hospitalizationDetailData['eventtime'] # 病例日期
                cases_data_copy['diagnosis'] = hospitalizationDetailData['diagnosis'] # 诊疗科目
                cases_data_copy['abstract'] = hospitalizationDetailData['abstract'] # 病症分类
                cases_data_copy['temperature'] = hospitalizationDetailData['temperature'] # 体温
                cases_data_copy['weight'] = hospitalizationDetailData['weight'] # 体重
                cases_data_copy['breathe'] = hospitalizationDetailData['breathe'] # 呼吸
                cases_data_copy['heartrate'] = hospitalizationDetailData['heartrate'] # 心率
                cases_data_copy['crt'] = hospitalizationDetailData['crt'] # crt
                cases_data_copy['tongkong'] = hospitalizationDetailData['tongkong'] # 瞳孔
                cases_data_copy['chiefnote'] = hospitalizationDetailData['chiefnote'] # 主诉记录
                cases_data_copy['checknote'] = hospitalizationDetailData['checknote'] # 检验分析
                cases_data_copy['carenote'] = hospitalizationDetailData['carenote'] # 护理记录
                cases_data_copy['processnote'] = hospitalizationDetailData['processnote'] # 处理治疗
                cases_data_copy['physicalorder'] = hospitalizationDetailData['physicalorder'] # 医嘱
                cases_data_copy['conditionnote'] = hospitalizationDetailData['conditionnote'] # 病情诊断
                cases_data_copy['visitrecord'] = hospitalizationDetailData['visitrecord'] # 回访记录
                cases_data_copy['hospitalnode'] = hospitalizationDetailData['hospitalnode'] # 住院病情
                cases_data_copy['sameclinic'] = hospitalizationDetailData['sameclinic'] # 疑似病例
                cases_data_copy['healthcheck'] = json.dumps(hospitalizationDetailData['healthcheck']) # 体格检查内容
                cases_data_copy['service_employee_id'] = hospitalizationDetailData['service_employee_id'] # 服务人员ID
                cases_data_copy['service_employee_name'] = hospitalizationDetailData['service_employee_name'] # 服务人员名称
                cases_data_copy['file_description'] = hospitalizationDetailData['file_description'] # 附件描述
                cases_data_copy['group_id'] = hospitalizationDetailData['group_id'] # 病例组ID
                cases_data_copy['state'] = hospitalizationDetailData['state'] # 病例状态
                cases_data_copy['open_appointment'] = hospitalizationDetailData['open_appointment'] # 是否开启预约
                cases_data_copy['appointment_time'] = hospitalizationDetailData['appointment_time'] # 预约时间
                cases_data_copy['is_share'] = hospitalizationDetailData['is_share'] # 是否和小程序共享查看病例
                cases_data_copy['blood_pressure'] = hospitalizationDetailData['blood_pressure'] # 血压
                cases_data_copy['surgical_record'] = hospitalizationDetailData['surgical_record'] # 手术记录
                cases_data_copy['is_apply'] = hospitalizationDetailData['is_apply'] # 申请/未申请
                # select_model 创建来源病历进行程（主诉、体况检查、检验分析、诊断治疗、医嘱/回访）字段无法匹配
                # whethertotransfer 是否为转过来的病历 无参数
                cases_data_copy['feeding_method'] = json.dumps(hospitalizationDetailData['feeding_method']) # 喂养方式
                cases_data_copy['feeding_frequency'] = hospitalizationDetailData['feeding_frequency'] # 喂养频次
                cases_data_copy['food_changes'] = hospitalizationDetailData['food_changes'] # 食物改变
                cases_data_copy['vaccine_status'] = json.dumps(hospitalizationDetailData['vaccine_status']) # 疫苗状态
                cases_data_copy['deworming_status'] = json.dumps(hospitalizationDetailData['deworming_status']) # 驱虫状态
                cases_data_copy['previous_medical_records'] = hospitalizationDetailData['previous_medical_records'] # 既往病例
                cases_data_copy['mentality'] = hospitalizationDetailData['mentality'] # 精神状态
                cases_data_copy['mentality_other'] = hospitalizationDetailData['mentality_other'] # 精神状态其他
                cases_data_copy['visible_mucosa'] = json.dumps(hospitalizationDetailData['visible_mucosa']) # 可视黏膜
                cases_data_copy['physical_condition_score'] = hospitalizationDetailData['physical_condition_score'] # 体况评分
                cases_data_copy['muscle_score'] = hospitalizationDetailData['muscle_score'] # 肌肉评分
                cases_data_copy['periodontal_score'] = hospitalizationDetailData['periodontal_score'] # 牙周评分
                cases_data_copy['heart_lung'] = json.dumps(hospitalizationDetailData['heart_lung']) # 心肺听诊
                cases_data_copy['abdomen'] = json.dumps(hospitalizationDetailData['abdomen']) # 腹部触诊
                cases_data_copy['lymph_gland'] = json.dumps(hospitalizationDetailData['lymph_gland']) # 淋巴结触诊
                cases_data_copy['skin_elasticity'] = hospitalizationDetailData['skin_elasticity'] # 皮肤弹性
                cases_data_copy['eye_condition'] = hospitalizationDetailData['eye_condition'] # 眼睛情况
                cases_data_copy['oral_mucosa'] = hospitalizationDetailData['oral_mucosa'] # 口腔粘膜
                cases_data_copy['suspected_illness'] = hospitalizationDetailData['suspected_illness'] # 疑似病症
                cases_data_copy['eyes'] = hospitalizationDetailData['eyes'] # 眼睛
                cases_data_copy['nose'] = hospitalizationDetailData['nose'] # 鼻部
                cases_data_copy['ears'] = hospitalizationDetailData['ears'] # 耳朵
                cases_data_copy['muscle'] = hospitalizationDetailData['muscle'] # 肌肉
                cases_data_copy['skin'] = hospitalizationDetailData['skins'] # 皮肤
                cases_data_copy['nerve'] = hospitalizationDetailData['nerve'] # 神经
                cases_data_copy['urology'] = hospitalizationDetailData['urology'] # 泌尿
                cases_data_copy['oral_cavity'] = hospitalizationDetailData['oral_cavity'] # 口腔
                cases_data_copy['is_vaccine'] = hospitalizationDetailData['is_vaccine'] # 未选/未/已经
                cases_data_copy['is_deworming'] = hospitalizationDetailData['is_deworming'] # 未选/未/已经
                cases_data_copy['clinical_examination'] = hospitalizationDetailData['clinical_examination'] # 临床检查
                cases_data_copy['case_level'] = hospitalizationDetailData['case_level'] # -
                cases_data_copy['present_history'] = hospitalizationDetailData['present_history'] # -
                try: # -
                    cases_data_copy['is_tw'] = hospitalizationDetailData['is_tw']
                except Exception:
                    cases_data_copy['is_tw'] = 0
                try: # rft
                    cases_data_copy['evet_rft'] = hospitalizationDetailData['evet_rft']
                except Exception:
                    cases_data_copy['evet_rft'] = ''

                csv_file8 = './医院数据/病例信息.csv'
                # 检查文件是否存在且不为空
                file_exists = os.path.isfile(csv_file8) and os.path.getsize(csv_file8) > 0
                # 保存到.csv文件中
                with open(csv_file8,'a',encoding='utf-8',newline='') as f:
                    # 将文件对象转换成 DictWriter 对象
                    writer = csv.DictWriter(f,fieldnames = cases_data.keys())
                    # 如果文件是新创建的，写入表头
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(cases_data_copy)







# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --------------------------------------------------------------------------------------------
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








# 获取商品信息 successful
try:
    getProductData(product_data,product_catalog_data)
except Exception:
    logging.exception(f"商品信息 发生异常!")
    print(f"\n\n商品信息 发生异常!!!")
    traceback.print_exc()
    os.system("pause")


# ---------------------------------------------------------------------------------------------

customerListData = customer_data['Data']
if not isinstance(customerListData,list):
    customerListData = []

for customer in customerListData:
    # 判断是不是本店用户    
    if int(customer['is_chain']) == 1:  # 只爬取本店信息
        continue

    # if int(customer['id']) != 657:  # 测试用户
    #     continue
    
    # user_head_CSV = ['task_id','owner_id','owner_name','owner_gender','owner_vip_level','owner_phone1','owner_phone2','owner_deposit','owner_integral','owner_address','owner_reg_date','owner_remarks','owner_source','sale_state','is_customer','hospital_id','hospital_code','hospital_name']
    
    logging.info(f'正在采集当前客户信息：' + str(customer['id']) + '-' + customer['name'] + '!')

    print('正在采集客户：' + str(customer['id']) + '-' + customer['name'] + ' 数据中！！！')
    
    try: # 获取客户信息 successful
        getCustomerData(customer,user_data,pet_data,card_data) 
    except Exception:
        logging.exception(f"获取客户信息-宠物信息 发生异常!")
        print(f"\n\n获取客户信息-宠物信息 发生异常!!!")
        traceback.print_exc()
        os.system('pause')
        break
        



    print("获取消费记录中···") # 获取当前客户：宠物编号的消费记录！！！
    try: # 获取消费记录 successful
        getExpenseCalendarData(customer)
    except Exception:
        logging.exception(f"获取消费记录 发生异常!")
        print(f"\n\n获取消费记录 发生异常!!!")
        traceback.print_exc()
        os.system('pause')
        break



    print("获取疫苗驱虫信息中···")
    try: # 获取疫苗驱虫信息 successful
        getVaccineData(customer,vaccine_data,vaccine_detail_data)
    except Exception:
        logging.exception(f"疫苗驱虫信息 发生异常!")
        print(f"\n\n疫苗驱虫信息 发生异常!!!")
        traceback.print_exc()
        os.system('pause')
        break



    print("获取病例信息中···")
    try: # 获取病例信息 successful
        getCasesData(customer,cases_data)
    except Exception:
        logging.exception(f"获取病例信息 发生异常!")
        print(f"\n\n获取病例信息 发生异常!!!")
        traceback.print_exc()
        os.system('pause')
        break




print("数据导出完毕！！!")
os.system("pause")


