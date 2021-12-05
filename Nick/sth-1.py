import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')
soup_lib = {}
carrots = soup.find_all('span', class_='text')#quotes
onions = soup.find_all('small', class_='author')#authors

print('    ')
'''
for carrot in carrots:
    print(carrot.text)

print('   ')

for onion in onions:
    print(onion.text)
'''

for i in range(len(carrots)):
    soup_lib[onions[i].text] = carrots[i].text

with open('sth-1.json', 'w', encoding='utf-8') as file:
    json.dump(soup_lib, file)


print(soup_lib)