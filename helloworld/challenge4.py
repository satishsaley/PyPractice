__author__ = 'satish'
__author__ = 'satish'
import urllib
import re


filehandle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.html")
mark = "nothing"
flag = 0
filtered = ""
r = object()
counter = 0
for lines in filehandle.readlines():
    if "nothing" in lines:
        print "ok"
        r = re.findall(r'((nothing))*$', lines)
        print lines.find('nothing')
        print r
print filtered