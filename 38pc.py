# requests库用于对http进行请求
import requests
# 用于处理网络波动、服务器繁忙、请求失败、重传间隔等操作
from requests.adapters import HTTPAdapter, Retry
# 导入pandas库主要用于对表格进行爬取
import pandas as pd
# 用于对字符串进行操作，可以读取、写入和修改字符串
from io import StringIO
# 用于解析url
from urllib.parse import urlsplit, urljoin
# 网络爬虫的解析库(对于HTML或者xml数据进行解析)
from bs4 import BeautifulSoup
# 正则表达式——用于字符串匹配和替换字符串
import re
server = "http://rest.ensembl.org"
# 建立网络请求会话，从客户端连接到服务器开始到断开
session = requests.Session()
# 创建适配器对象
adapter = HTTPAdapter(
# 限流算法的实现
max_retries=Retry(
backoff_factor=3600 / 55000,#重传时间间隔
respect_retry_after_header=True,#Http的响应标头
status_forcelist=[429],#429表示请求太多，重传
allowed_methods=["GET", "POST"],#对get、post的http方法下设置限流
)
)
# 为特定协议和主机设置自定义请求的适配器，方便发送和处理HTTP请求
session.mount(server, adapter)

# 使用get方法返回response对象
response=session.get(server)
# 使用BeautifulSoup库对http请求返回的对象进行解析
soup=BeautifulSoup(response.text, 'lxml')
urls=[]
# 使用BeautifulSoup库中的CSS选择器进行爬虫，获取接口的url地址
for i in soup.select("body > div > table > tbody > tr > td > a"):
# append()在列表的末尾添加新的元素
    urls.append(i.get("href"))
    print(i.get("href"))


# 有必选参数
def func0(url):
    # 响应头在Chrome浏览器的网页上：右键 ——> 检查 ——> Network ——> Doc ——> 在 Name 里找到对应的请求文件 ——> 在右边选择 Headers 标签页，找到“Request Headers”，就可以看到我们发送给服务器的 headers。
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    # 使用get方法传入url等参数进去具体接口详情页，获取返回对象
    response=session.get(url, headers=headers)
    # 使用read_html方法获取表格数据，转化为DFrame对象
    df0=pd.read_html(StringIO(response.text))[0]#第一个表格
    df1=pd.read_html(StringIO(response.text))[1]
    # df2=pd.read_html(StringIO(response.text))[2]
    # 解析接口详细页面
    soup=BeautifulSoup(response.text, 'lxml')
    # 遍历表格name列的列表获取必选参数，通过",".join把必选参数通过,隔开方式，拼接在一起为一个新的字符串
    # tolist()是返回一个列表
    # f格式{}嵌入遍历得到的变量
    required=", ".join(f"{i}: str" for i in [i for i in df0["Name"].tolist()])
    optional=", ".join(i for i in [f"{i}=None" for i in df1["Name"].tolist()])
    # 拼接字符,dict是字典,是一种无序的可变的序列.每一个键值之间用:隔开
    params="params=dict("+", ".join(f"{i}={i}" for i in [i for i in df1["Name"].tolist()])+")"
    for i in soup.select("#title"):
        # 如果开头匹配到是get
        # startswith判断字符串以什么开头
        if i.text.startswith("GET "):
            # re.sub正则表达式用于替换字符串
            # r原生字符串
            # \w匹配多个字母下划线
            # \1反向引用,引用以前已经匹配到字符串
            # removeprefix去除指定的前缀
            # https://rest.ensembl.org/archive/id/需要的
            # https://rest.ensembl.org/documentation/info/archive_id_get
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("GET "))
            # urlsplit(url).path.split("/")[-1]
            # 解析url地址,以"/"分割后提取最后的部分作为函数名
            # f是格式化字符串,可以在字符串中添加变量的值
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"("+required+","+optional+")"+":"+"\n"+'  print(requests.get('+f'f"https://rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+","+").json())"

        elif i.text.startswith("POST "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("POST "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"(id: List[str],"+required+","+optional+")"+":"+"\n"+'  print(requests.post('+f'f"https://rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+',json={"ids": id},'+").json())"


# 无必选参数
# 读取表格不同
def func1(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    response=session.get(url, headers=headers)
    df0=pd.read_html(StringIO(response.text))[0]
    optional=", ".join(i for i in [f"{i}=None" for i in df0["Name"].tolist()])
    params="params=dict("+", ".join(f"{i}={i}" for i in [i for i in df0["Name"].tolist()])+")"
    # df1=pd.read_html(StringIO(response.text))[1]
    soup=BeautifulSoup(response.text, 'lxml')
    for i in soup.select("#title"):
        if i.text.startswith("GET "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("GET "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"("+optional+")"+":"+"\n"+'  print(requests.get('+f'f"https://rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+","+").json())"
        elif i.text.startswith("POST "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("POST "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"(id: List[str],"+optional+")"+":"+"\n"+'  print(requests.post('+f'f"https://rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+',json={"id": id},'+").json())"
# Archive
# print(func0(urls[0]))
# print(func1(urls[1]))

# Comparative Genomics     
# print(func0(urls[2]))
# print(func0(urls[3]))
# print(func0(urls[4]))
# print(func0(urls[5]))
# print(func0(urls[6]))
# print(func0(urls[7]))
# print(func0(urls[8]))
# print(func0(urls[9]))
# print(func0(urls[10]))
# print(func0(urls[11]))
# print(func0(urls[12]))
# print(func0(urls[13]))

# Cross References
# print(func0(urls[14]))
# print(func0(urls[15]))
# print(func0(urls[16]))

# Information
# print(func0(urls[17]))
# print(func0(urls[18])) 
# print(func0(urls[19]))
# print(func0(urls[20])) 
# 没有必选参数
# print(func1(urls[21]))
# print(func0(urls[22])) 
# 没有必选参数
# print(func1(urls[23]))
# print(func0(urls[24]))
# 没有必选参数
# print(func1(urls[25]))
# print(func1(urls[26]))
# print(func1(urls[27]))
# print(func0(urls[28]))
# 没有必选参数
# print(func1(urls[29]))
# print(func0(urls[30]))
# print(func0(urls[31]))
# print(func0(urls[32]))
# print(func0(urls[33]))
# print(func0(urls[34]))
# 没有参数
# print(func1(urls[35]))
# print(func1(urls[36]))
# print(func1(urls[37]))
# print(func1(urls[38]))
# 有必选参数
# print(func0(urls[39]))
# 没有参数
# print(func1(urls[40]))
# 出错--41
# print(func0(urls[41]))
# print(func0(urls[42]))

# Linkage Disequilibrium
# print(func0(urls[43]))
# print(func0(urls[44]))
# print(func0(urls[45]))

# Lookup
# print(func0(urls[46]))
# 没有必须参数post
# print(func1(urls[47]))
# print(func0(urls[48]))
# print(func0(urls[49]))

# Mapping
# print(func0(urls[50]))
# print(func0(urls[51]))
# print(func0(urls[52]))
# print(func0(urls[53]))

# Ontologies and Taxonomy
# print(func0(urls[54]))
# print(func0(urls[55]))
# print(func0(urls[56]))
# print(func0(urls[57]))
# print(func0(urls[58]))
# print(func0(urls[59]))
# print(func0(urls[60]))
# print(func0(urls[61]))

# Overlap
# print(func0(urls[62]))
# print(func0(urls[63]))
# print(func0(urls[64]))

# Phenotype annotations
# print(func0(urls[65]))
# print(func0(urls[66]))
# print(func0(urls[67]))
# print(func0(urls[68]))

# Regulation
# print(func0(urls[69]))
# print(func0(urls[70]))
# print(func0(urls[71]))
# print(func0(urls[72]))
# print(func0(urls[73]))
# print(func0(urls[74]))
# print(func0(urls[75]))

# Sequence
# print(func0(urls[76]))
# print(func1(urls[77]))
# print(func0(urls[78]))
# print(func0(urls[79]))

# Transcript Haplotypes
# print(func0(urls[80]))

# VEP
# print(func0(urls[81]))
# print(func0(urls[82]))
# print(func0(urls[83]))
# print(func0(urls[84]))
# print(func0(urls[85]))
# print(func0(urls[86]))

# Variation
# print(func0(urls[87]))
# print(func0(urls[88]))
# print(func0(urls[89]))
# print(func0(urls[90]))
# print(func0(urls[91]))
# print(func0(urls[92]))

# Variation GA4GH
# print(func1(urls[93]))
# print(func0(urls[94]))--问题
# print(func0(urls[95]))
# print(func0(urls[96]))
# print(func0(urls[97]))
# print(func0(urls[98]))
# print(func0(urls[99]))
# print(func1(urls[100]))
# print(func0(urls[101]))
# print(func0(urls[102]))
# print(func0(urls[103]))
# print(func0(urls[104]))
# print(func0(urls[105]))--有问题
# print(func0(urls[106]))
# print(func0(urls[107]))
# print(func0(urls[108]))
# print(func0(urls[109]))
# print(func0(urls[110]))
# print(func1(urls[111]))
# print(func0(urls[112]))
# print(func0(urls[113]))
# print(func0(urls[114]))
