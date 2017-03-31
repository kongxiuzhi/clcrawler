#coding:utf-8

import re
from urllib import request
from http.cookiejar import MozillaCookieJar
import gzip
import threading
import socket


def pagelingre(line,rules):
    pattern = re.compile(rules)
    link = pattern.findall(line)
    if link:
        return link[0]
    else:
        return None


def getpagelink(clfile,rules,page=1):
    pagelinks=[]
    with open(file=clfile,mode='r',errors='None') as f:
        for line in f:
            link = pagelingre(line,rules)
            if link and page:
                pagelinks.append(baselink+link)
            elif link and not page:
                pagelinks.append(link)
    return pagelinks




def unzip(rawdata,clfile,i=0):
    data = gzip.decompress(rawdata)
    with open(file=clfile,mode='a') as f:
        f.write(data.decode(encoding='utf-8',errors="ignore"))
    return "%s page is ok"%(i+1)

headers = {
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Host':'cl.bvaz.club',
   'Referer':'http://cl.bvaz.club/index.php',
   'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language':'en-US,en;q=0.5',
   'Accept-Encoding':'gzip, deflate',
   'Connection':'keep-alive',
}
picfile = 'picfile.txt'
pagefile = 'pagefile.txt'
pagerules = r'<h3><a href="(htm_data.*?)".*?>'
picrules = r'<input.*?src="(.*?jpg)".*?>'
page = 5
baselink = 'http://cl.bvaz.club/'
url='http://cl.bvaz.club/thread0806.php?fid=8&search=&page='
cookiefile='clcookies.txt'
urls = []
for i in range(1,page):
    urls.append(url+str(i))



cookie = MozillaCookieJar(cookiefile)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
request.install_opener(opener)
for i in range(page-1):
    req = request.Request(urls[i],headers=headers)
    try:
        raw = request.urlopen(url=req,timeout=10).read()
    except socket.timeout as e:
        print(e)
        continue
    data = unzip(raw,pagefile,i)
    print(data)

cl = getpagelink(pagefile,pagerules)
for i in cl:
    req = request.Request(i,headers=headers)
    try:
        raw = request.urlopen(url=req,timeout=10).read()
    except socket.timeout as e:
        print(e)
        continue
    data = unzip(raw,picfile)
    print(i)    
picl = getpagelink(picfile,picrules,0)

'''
class DLpic(threading.Thread):
    def __init__(lock,name,url):
        super(DLpic,self).__init__()
        self.lock = lock
        self.name = name
        self.url = url
    def run(self):
        
   '''     
        



for i in picl:
    print(i)
