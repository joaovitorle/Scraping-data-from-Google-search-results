from google import google
num_pages = 1
lang = 'pt'
area = 'com'

search_results = google.search('Doações coronavírus em São Bernardo do Campo', num_pages, lang, area)

for results in search_results:



    print(results.description)
    print(results.link)

