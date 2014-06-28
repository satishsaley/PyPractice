__author__ = 'satish'
import urllib
import re


filehandle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
mark = "<!--"
flag = 0
filtered = ""
r = object()
counter = 0
for lines in filehandle.readlines():
    if mark in lines and flag == 0:
        print "mark found"
        flag = 1
    elif flag == 1:
        #r = getalphabet(lines)
        filtered = filtered + "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", lines))

print filtered