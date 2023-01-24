#LC20lb MBeuO DKV0Md


import requests,sys,bs4,pyperclip

# get the search text from clip board


address = pyperclip.paste()



res = requests.get('https://www.google.com/search?q='+address)
print(res.status_code)
test = bs4.BeautifulSoup(res.text,'html.parser')


elems = test.select('h3')

try:
    i=0
    while i<100000:
        print(elems[i].text)
        i += 1
except:
  print("")
