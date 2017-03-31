import re

# text = '<h3><a href="htm_data/8/1703/2325748.html" target="_blank" id="">.342<a><h3>'

baselink = 'cl.bvaz.club/'

def pagelingre(line):
    rules = r"<input.*?src='(.*?)'.*?>"
    pattern = re.compile(rules)
    link = pattern.findall(line)
    if link:
        return link[0]
    else:
        return None


def getpagelink():
    pagelinks=[]
    with open(file='picfile.txt',mode='r',errors='None') as f:
        for line in f:
            link = pagelingre(line)
            if link:
                pagelinks.append(link)
    return pagelinks

cl = getpagelink()
for i in cl:
    print(i)
