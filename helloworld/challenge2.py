import urllib

def getAplhabet(lines):
    newlist = []
    for i in xrange(0, len(lines)- 1) :
        if ord(lines[i]) >= 97 and ord(lines[i]) <= 122 :
            newlist.append(lines[i])

    if len(newlist) == 0:
        return
    print newlist
    return newlist


__author__ = 'satish'
filehandle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
mark = "%%$@_$^__#)"
flag = 0
filtered = []
for lines in filehandle.readlines():
    if mark in lines and flag == 0:
        flag = 1
    elif flag == 1:
        filtered.append(getAplhabet(lines))
        #print filtered






