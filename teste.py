import requests

from bs4 import BeautifulSoup

user_input= input('O que deseja pesquisar: ')
print('Googling.....')

google_search = requests.get('https://www.google.com/search?q='+user_input)
soup = BeautifulSoup(google_search.text, 'html.parser')


print(soup)