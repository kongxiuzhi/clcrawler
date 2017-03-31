#coding:utf-8

import re
from urllib import request
from http.cookiejar import MozillaCookieJar
import gzip


def unzip(rawdata):
    data = gzip.decompress(rawdata)
    with open('zhihu.txt','a') as f:
        f.write(data.decode('utf-8'))
    return 'ok'

headers = {
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Host':'www.zhihu.com',
   'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language':'en-US,en;q=0.5',
   'Accept-Encoding':'gzip, deflate, br',
   'Connection':'keep-alive',
}
data ={}
url='https://www.zhihu.com/question/46404678'
cookiefile='cookies.txt'

cookie = MozillaCookieJar(cookiefile)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
request.install_opener(opener)
req = request.Request(url,headers=headers)

raw = request.urlopen(req).read()
data = unzip(raw)
print(data)
