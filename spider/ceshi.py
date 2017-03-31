
#coding:utf-8

import re
from urllib import request
from http.cookiejar import MozillaCookieJar
import gzip
import threading
import socket
import time

socket.setdefaulttimeout(20)
picfile = "other/picfile6.txt"
picrules = r'src="(.*?[jpg|gif|png])"'
#picrules = r"<input.*?src='(.*?[jpg|gif|png])'.*?type='image'.*?>"
#picrules = r'<img.*?src="(.*?gif)".*?>'
#picrules = r"<input.*?src='(.*?g)'.*?>"
#picrules = r'<input.*?src="(.*?g)".*?>'
localdir = "/home/king/Pictures/dongman/"


class Dlpic(threading.Thread):
    def __init__(self,url,name):
        super(Dlpic,self).__init__()
        self.url = url
        self.name = name
    def run(self):
        try:
            print(self.url)
            request.urlretrieve(self.url,localdir+str(self.name)+'.gif')
        except:
            print(str(self.name)+'error')

def pagelingre(line,rules):
    pattern = re.compile(rules)
    link = pattern.findall(line)
    if link:
        return link
    else:
        return None


def getpagelink(clfile,rules):
    with open(file=clfile,mode='r',errors='None') as f:
        lines = f.read()
        if lines:
            link = pagelingre(lines,rules)
            if link: 
                link = ['http://img5.uploadhouse.com/fileuploads/23117/231170457d638848be7645566c4edc7b0872be2c.gif']
                return link

picl = getpagelink(picfile,picrules)
count = 0
end = len(picl)
print(end)
for i in picl:
    dpt = Dlpic(i,count)
    dpt.start()
    dpt.join(4)
    count +=1
time.sleep(60)
print("over")
