import urllib, re, time
from BeautifulSoup import *

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

html = urllib.urlopen(url).read()

(header, trash) = html.split('<!--', 1)
(header, trash) = trash.split('<!--', 1)

#sprint trash

for i in range(0, len(trash)):
    if (ord(trash[i]) > 64 and ord(trash[i]) < 91) or (ord(trash[i]) > 96 and ord(trash[i]) < 123):
        print trash[i],
