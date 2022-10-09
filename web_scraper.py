import requests

from bs4 import BeautifulSoup

url = 'https://www.linkedin.com'

r = requests.get(url)
soupe = BeautifulSoup(r.content, 'lxml')
title = soupe.find_all('DevOps')

print(title)
print(r)

InV%2@17lbV.