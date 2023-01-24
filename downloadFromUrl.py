# To Download files from the internet 

import requests

url = 'https://gaadiwaadi.com/wp-content/uploads/2022/09/modified-mahindra-thar-16.jpg'
res = requests.get('https://gaadiwaadi.com/wp-content/uploads/2022/09/modified-mahindra-thar-16.jpg')
print(type(res))
open('modified-mahindra-thar-16.jpg','wb').write(res.content)
print(res.status_code)