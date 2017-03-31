import re

# text = '<h3><a href="htm_data/8/1703/2325748.html" target="_blank" id="">.342<a><h3>'

baselink = 'cl.bvaz.club/'

def pagelingre(line):
    rules = r'<h3><a href="(htm_data.*?)".*?>'
    pattern = re.compile(rules)
    link = pattern.findall(line)
    if link:
        return link[0]
    else:
        return None


def getpagelink():
    pagelinks=[]
    with open(file='cl.txt',mode='r',errors='None') as f:
        for line in f:
            link = pagelingre(line)
            if link:
                pagelinks.append(baselink+link)
    return pagelinks

cl = getpagelink()
with open('clpagelink.txt','w') as f:
    f.write(str(cl)[1:-1])


with open('clpagelink.txt','r') as f:
    cls = f.read()
    for i in cls:
        print(i) 

