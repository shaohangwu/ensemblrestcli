import requests
from requests.adapters import HTTPAdapter, Retry
import pandas as pd
from io import StringIO
from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup
import re
server = "http://grch37.rest.ensembl.org"
session = requests.Session()
adapter = HTTPAdapter(
max_retries=Retry(
backoff_factor=3600 / 55000,
respect_retry_after_header=True,
status_forcelist=[429],
allowed_methods=["GET", "POST"],
)
)
session.mount(server, adapter)
response=session.get(server)
soup=BeautifulSoup(response.text, 'lxml')
urls=[]
for i in soup.select("body > div > table > tbody > tr > td > a"):
    urls.append(i.get("href"))

# for i in urls:
#     print(i)

# 有必选参数
def func0(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    response=session.get(url, headers=headers)
    df0=pd.read_html(StringIO(response.text))[0]
    df1=pd.read_html(StringIO(response.text))[1]
    # df2=pd.read_html(StringIO(response.text))[2]
    soup=BeautifulSoup(response.text, 'lxml')
    required=", ".join(f"{i}: str" for i in [i for i in df0["Name"].tolist()])
    optional=", ".join(i for i in [f"{i}=None" for i in df1["Name"].tolist()])
    params="params=dict("+", ".join(f"{i}={i}" for i in [i for i in df1["Name"].tolist()])+")"
    for i in soup.select("#title"):
        if i.text.startswith("GET "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("GET "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"("+required+","+optional+")"+":"+"\n"+'  print(requests.get('+f'f"https://grch37.rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+","+").json())"

        elif i.text.startswith("POST "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("POST "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"(id: List[str],"+required+","+optional+")"+":"+"\n"+'  print(requests.post('+f'f"https://grch37.rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+',json={"ids": id},'+").json())"


# 无必选参数

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
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"("+optional+")"+":"+"\n"+'  print(requests.get('+f'f"https://grch37.rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+","+").json())"
        elif i.text.startswith("POST "):
            endpoint=re.sub(r":(\w+)", r"{\1}", i.text.removeprefix("POST "))
            return "@app.command()"+"\n"+"def "+urlsplit(url).path.split("/")[-1]+"(id: List[str],"+optional+")"+":"+"\n"+'  print(requests.post('+f'f"https://grch37.rest.ensembl.org/{endpoint}"'+", "+'headers={"Content-Type": "application/json"}'+","+params+',json={"id": id},'+").json())"
# Archive
# print(func0(urls[0]))
# print(func1(urls[1]))

# Comparative Genomics     
# print(func0(urls[2]))
# print(func0(urls[3]))
# print(func0(urls[4]))
# print(func0(urls[5]))

# Cross References
# print(func0(urls[6]))
# print(func0(urls[7]))
# print(func0(urls[8]))

# Information
# print(func0(urls[9]))
# print(func0(urls[10]))
# print(func0(urls[11]))
# print(func0(urls[12]))
# print(func1(urls[13]))
# print(func0(urls[14]))
# print(func1(urls[15]))
# print(func0(urls[16]))
# print(func1(urls[17]))
# print(func1(urls[18])) 
# print(func0(urls[19]))
# print(func1(urls[20])) 
# 没有必选参数
# print(func1(urls[21]))
# print(func1(urls[22])) 
# 没有必选参数
# print(func1(urls[23]))
# print(func0(urls[24]))
# 没有必选参数
# print(func1(urls[25]))
# print(func0(urls[26]))
# print(func0(urls[27]))

# Linkage Disequilibrium
# print(func0(urls[28]))
# print(func0(urls[29]))
# print(func0(urls[30]))

# Lookup
# print(func0(urls[31]))
# print(func1(urls[32]))
# print(func0(urls[33]))
# print(func0(urls[34]))

# Mapping 
# print(func0(urls[35]))
# print(func0(urls[36]))
# print(func0(urls[37]))
# print(func0(urls[38]))

# Ontologies and Taxonomy
# print(func0(urls[39]))
# print(func0(urls[40]))
# print(func0(urls[41]))
# print(func0(urls[42]))
# print(func0(urls[43]))
# print(func0(urls[44]))
# print(func0(urls[45]))
# print(func0(urls[46]))

# Overlap
# print(func0(urls[47]))
# print(func0(urls[48]))
# print(func0(urls[49]))

# Phenotype annotations
# print(func0(urls[50]))
# print(func0(urls[51]))
# print(func0(urls[52]))
# print(func0(urls[53]))

# Regulation
# print(func0(urls[54]))
# print(func0(urls[55]))
# print(func0(urls[56]))
# print(func0(urls[57]))
# print(func0(urls[58]))
# print(func0(urls[59]))
# print(func0(urls[60]))

# Sequence
# print(func0(urls[61]))
# print(func1(urls[62]))
# print(func0(urls[63]))
# print(func0(urls[64]))

# Transcript Haplotypes
# print(func0(urls[65]))

# VEP
# print(func0(urls[66]))
# print(func0(urls[67]))
# print(func0(urls[68]))
# print(func0(urls[69]))
# print(func0(urls[70]))
# print(func0(urls[71]))

# Variation
# print(func0(urls[72]))
# print(func0(urls[73]))
# print(func0(urls[74]))
# print(func0(urls[75]))
# print(func0(urls[76]))
# print(func0(urls[77]))

# Variation GA4GH
# print(func1(urls[78]))
# print(func0(urls[79]))
# print(func0(urls[80]))
# print(func0(urls[81]))
# print(func0(urls[82]))
# print(func0(urls[83]))
# print(func0(urls[84]))
# print(func1(urls[85]))
# print(func0(urls[86]))
# print(func0(urls[87]))
# print(func0(urls[88]))
# print(func0(urls[89]))
# print(func0(urls[90]))
# print(func0(urls[91]))
# print(func0(urls[92]))
# print(func0(urls[93]))
# print(func0(urls[94]))
# print(func0(urls[95]))
# print(func1(urls[96]))
# print(func0(urls[97]))
# print(func0(urls[98]))
# print(func0(urls[99]))