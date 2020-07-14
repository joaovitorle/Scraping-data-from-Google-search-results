from google import google
num_pages = 1
lang = 'pt'
area = 'com'

pesquisa= input('O que você deseja pesquisar: ')

search_results = google.search(pesquisa, num_pages, lang, area)

for results in search_results:

    analise= 'Antony' in results
    if analise == True:
        print(results.description+1)
        print(results.link+1)

    else:
        print(results.description)
        print(results.link)



