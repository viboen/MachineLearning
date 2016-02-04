import urllib, re
import pickle, pprint
from BeautifulSoup import *

'''
ocr
equality
linkedlist.php
peak.html
channel.html
'''

url = 'http://www.pythonchallenge.com/pc/def/'
url_change = 'peak.html'

def connect(url):
    return BeautifulSoup(urllib.urlopen(url).read())
    

soup = connect(url+url_change)

# Retrieve all of the anchor tags
tags = soup('peakhell')
url_change = re.findall('[a-zA-Z]+\.[a-zA-Z]', str(tags))

connection = urllib.urlopen(url+url_change[0])
connection = connection.read()
#print connection

pfile = open('banner.p', 'w')
pfile.write(connection)
pfile.close()

with open('banner.p', 'rb') as file:
  file = pickle.load(file)
  print file
  for line in file:
    print("".join(a * b for a, b in line))

'''
for i in range(0, len(data)):
    for x in range(0, len(data[i])):
            #print data[i][x][0:]
            data = data


while True:
    data = connect(url)
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    numbers = re.findall('[0-9]+', data)
    if len(numbers) > 0: url = url + numbers[0]
    else: 
        print data
        break
'''                   