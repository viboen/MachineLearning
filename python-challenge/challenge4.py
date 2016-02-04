import urllib, re

'''
ocr
equality
linkedlist.php
peak.html
'''

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def connect(url):
    link = urllib.urlopen(url)
    return link.read()

while True:
    data = connect(url)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    numbers = re.findall('[0-9]+', data)
    if len(numbers) > 0: url = url + numbers[0]
    else: 
        print data
        break

