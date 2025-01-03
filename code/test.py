from bs4 import BeautifulSoup

# 假设html是你要解析的HTML内容
html = """
<html>
  <body>
    <h3>标题1</h3>
    <p>这是标题1后面的内容</p>
    <strong>强调1</strong>
    <strong>强调2</strong>
    <h3>标题2</h3>
    <p>这是标题2后面的内容</p>
    <strong>强调3</strong>
    <strong>强调4</strong>
  </body>
</html>
"""

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 找到指定的h3标签
target_h3 = soup.find('h3', text='标题1')

# 找到紧随该h3标签后的所有strong标签
strong_tags = []
for sibling in target_h3.find_next_siblings():
    # print()
    if sibling.name == 'strong':
        strong_tags.append(sibling)

# 打印结果
for tag in strong_tags:
    print(tag)
