from urllib import parse

url = "https://v.qq.com/x/search/?searchSession=tabid=%E5%85%A8%E9%83%A8%E9%A2%91%E9%81%93|0,%E7%94%B5%E8%A7%86%E5%89%A7|2,%E7%94%B5%E5%BD%B1|1,%E7%BB%BC%E8%89%BA|3,%E6%96%B0%E9%97%BB|11,%E7%BA%AA%E5%BD%95%E7%89%87|6,%E4%BD%93%E8%82%B2|14,%E9%9F%B3%E4%B9%90|5,%E6%B8%B8%E6%88%8F|17,%E5%8E%9F%E5%88%9B|8,%E8%B4%A2%E7%BB%8F|13,%E6%95%99%E8%82%B2|15,%E6%AF%8D%E5%A9%B4|20,%E5%B0%91%E5%84%BF|106,%E5%85%B6%E5%AE%83|7&firstTabid=%E5%85%A8%E9%83%A8|0,%E7%94%A8%E6%88%B7|103&q=%E7%A0%94%E5%AD%A6&preQid=BT4BsbSHpquP9olk3dKIAsFpPpHy6u63597ednrMzYehcZ0_toqeyg&queryFrom=3&cur=3&isNeedQc=true&_=1707040553453#!filtering=1"
query = parse.urlparse(url).query
params = dict(parse.parse_qsl(query))

print(params)
