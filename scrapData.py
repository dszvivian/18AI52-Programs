#Get all the players list from website 
# note: check for the class name --> line 11 it may vary

import requests,bs4

res = requests.get('https://www.footballdatabase.eu/en/players')
print(res.status_code)
test = bs4.BeautifulSoup(res.text,'html.parser')


elems = test.select('.name')

try:
    i=0
    while i<100:
        print(elems[i].text)
        i += 1
except:
  print("An exception occurred")
