import requests
from bs4 import BeautifulSoup
from google import google

num_pages = 1

search_results = google.search('Doações coronavírus São Bernardo do Campo', num_pages)

soup = BeautifulSoup(search_results,'lxml')
links = soup.find_all('doações')

for link in links:
    if "Prefeitura" in link.text:
        print(link)

