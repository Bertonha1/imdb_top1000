#%%
import requests
import random

# Inicializa a página
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MzU3MjNhNjhkZjJmZDAwOTVlNTc1NmVlZWFkMjBkYiIsIm5iZiI6MTcyOTM2MTAzOS4yNjQ0MjksInN1YiI6IjY3MTNmMjlhOTlmMjJmMzI2YWFkMjc1MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5QQfBKOrZWuzdH1631qbpsinpobmh1XEdMUW7_Hi2Lk"
}

lista_filmes = {}

# Loop para percorrer as páginas
for pages in range(1, 100):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={pages}"
    
    response = requests.get(url, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        # Exibe informações sobre os filmes encontrados
        for movie in data['results']:
            chave = movie['title']
            valor = movie['overview']
            lista_filmes[chave] = valor
    else:
        print(f"Erro na página {pages}: {response.status_code}")
        
        
#%%
# Escolhe 5 filmes aleatórios
filmes_aleatorios = random.sample(list(lista_filmes.keys()), 5)
# Cria um dicionário para os filmes aleatórios
elm_aleatorios = {
    f"Filme: {chave}\nDescrição: {lista_filmes[chave]}\n{'-' * 20}": lista_filmes[chave] 
    for chave in filmes_aleatorios
}
# Imprime os filmes aleatórios
for key in elm_aleatorios.keys():
    print(key)

# %%
lista_filmes

# %%
