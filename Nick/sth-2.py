import requests
import json
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')
soup_lib = {}
eve_all = soup.find_all('div', class_='card-body')
for e in eve_all:
    potatoes = soup.find_all('h4', class_='card-title')
    onions = soup.find_all('h5')
    carrots = soup.find_all('a', 'href')

for potato in potatoes:
    print(potato.text)
print('     ')
for onion in onions:
    print(onion.text)
for carrot in onions:
    print(carrot.text)
'''
for i in range(len(potatoes)):
    soup_lib[potatoes[i].text] = onions[i].text

with open('sth-2.json', 'w', encoding='utf-8') as file:
    json.dump(soup_lib, file)'''