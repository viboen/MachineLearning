import urllib, re, time
from BeautifulSoup import *

'''
ocr
equality
linkedlist
'''

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

html = urllib.urlopen(url).read()
#print html

(trash, text, trash) = html.split('--', 3)


#print text
'''
for i in range(3, len(trash)-3):
    if (ord(trash[i])<=122 and >= 97 and ) :
        print trash[i],
'''
letter = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', text)
print letter

