from urllib.parse import urlencode,unquote
from binascii import *
import re

a = "<input src='t.jpg'>"
b = "<input src='m.png'>"

pattern = re.compile(r"<input src='(.*?[jpg|png])'")


print(re.findall(pattern,a))
print(re.findall(pattern,b))

    

