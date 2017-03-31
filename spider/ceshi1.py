
#coding:utf-8

import re
from urllib import request
from http.cookiejar import MozillaCookieJar
import gzip
import threading
import socket
import time

socket.setdefaulttimeout(10)
picfile = "other/picfile4.txt"
picrules = r"<input.*?src='(.*?[jpg|gif|png])'.*?type='image'.*?>"
#picrules = r"<input.*?src='(.*?g)'.*?>"
#picrules = r'<input.*?src="(.*?g)".*?>'
localdir = "/home/king/Pictures/Arsia/"


class Dlpic(threading.Thread):
    def __init__(self,url,name):
        super(Dlpic,self).__init__()
        self.url = url
        self.name = name
    def run(self):
        try:
            print(self.url)
            if self.url[-3:]=='gif':
                request.urlretrieve(self.url,localdir+str(self.name)+'.gif')
            else:
                request.urlretrieve(self.url,localdir+str(self.name)+'.jpg')
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
