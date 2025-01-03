import requests
import csv
from bs4 import BeautifulSoup
import os


if not os.path.exists("中药"):  # 不存在则创建
    # 创建文件夹
    os.makedirs("中药")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


# 设置列表，存储药材的各种名称说明
drug_head_list = [
    "中药名",
    "别名",
    "英文名",
    "药用部位",
    "植物形态",
    "产地分布",
    "采收加工",
    "药材性状",
    "性味归经",
    "功效与作用",
    "临床应用",
    "药理研究",
    "主要成分",
    "使用禁忌",
    "配伍药方",
]
for page in range(1, 46):
    # 设置列表，存储每种药材的信息
    drug_list = []

    url = f"http://www.zhongyoo.com/name/page_{page}.html"
    res = requests.get(url, headers=headers)
    res.encoding = "gbk"  # 防止乱码

    bs = BeautifulSoup(res.text, "html.parser")
    div_sp_list = bs.find_all("div", class_="sp")
    for div_sp in div_sp_list:
        a = div_sp.find("strong").find("a")  # strong标签中的a标签

        href = a["href"]  # 中药详情链接
        drug_name = a.text  # 中药名称

        res_content = requests.get(href, headers=headers)
        res_content.encoding = "gbk"  # 防止乱码
        bs_content = BeautifulSoup(res_content.text, "html.parser")
        div_text_list = bs_content.find_all("div", class_="text")
        p_list = div_text_list[1].find_all("p")

        # 设置字典，存储药材的详细信息
        drug_dict = {}

        i = -1  # 遍历头部drug_head_list
        # 解析完成
        for p in p_list:
            strong = p.find("strong")
            if i == 11 and not strong and p.text:
                drug_dict["药理研究"] = drug_dict["药理研究"] + p.text.strip()
            elif not strong and p.text:
                if i == 14:
                    drug_dict["配伍药方"] = drug_dict["配伍药方"] + p.text.strip()
                else:
                    drug_dict["配伍药方"] = p.text.strip()
            if not strong:
                continue
            i += 1
            if i == 2:
                if strong.text[-1] not in "英文名":
                    drug_dict["英文名"] = None
                    i += 1

            if i == 15:
                break
            try:
                alias = p.text.split("】")[1].rstrip("。")
            except:
                alias = p.text.split("：")[1].rstrip("。")
            drug_dict[drug_head_list[i]] = alias

        drug_list.append(drug_dict)
        print(f"{drug_name}  解析完成")

    print(
        f"第  {page}  页爬取完成——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————"
    )

    # 保存到.csv文件中
    with open("./中药/中药信息.csv", "a", encoding="utf-8") as f:
        # 将文件对象转换成 DictWriter 对象
        write = csv.DictWriter(f, fieldnames=drug_head_list)
        # 写入表头与数据
        if i == 1:
            write.writeheader()
        write.writerows(drug_list)
