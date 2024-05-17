import functions_framework
from bs4 import BeautifulSoup as bs
import json
from google.cloud import storage
import requests
import time

@functions_framework.http
def extract_api(request):
    
    request_json = request.get_json() # recebe o request e transforma em um dicionário
    table = request_json['termo_pesquisa']  # Dentro do request seleciona o termo_pesquisa
    if not table:
        return 'Esta faltando o "termo_pesquisa" na sua requisição'

    # Concatenando url CNN com o termo de pesquisa
    url_principal = f"https://www.cnnbrasil.com.br/?s={table}"

    # Fazendo o get no html do site com as pesquisas em geral
    try:
        response = requests.get(url_principal)
        response.raise_for_status()
        soup = bs(response.content, 'html.parser') # Fazendo a soup html parser do bs4
    
    except requests.exceptions.RequestException as e:
        return f'Erro ao consultar o site : {e}'

    # Localizando links dos artigos
    quotes = soup.select("a.home__list__tag")
    listahref = [quote.get("href") for quote in quotes]  # Extraindo o href dos objetos de link

    extracted_data = []

    #Com os links extraidos, agora a extração sera em cima de cada um deles

    for link in listahref:
        #Estou reunindo os dados coletados em um dic, para facilitar na hora de transformar em json
        article_data = {}

        try:
            response = requests.get(link)
            response.raise_for_status()
            article_soup = bs(response.content, 'html.parser')

            # Extraindo Titulo, Subtitulo e Autor do artigo selecionado
            article_data["title"] = article_soup.select_one("h1.post__title").text.strip()
            article_data["subtitle"] = article_soup.select_one("p.post__excerpt").text.strip()
            article_data["author"] = article_soup.select_one("p.author__name span span").text.strip()

        except requests.exceptions.RequestException as e:
            print(f'Erro ao extrair dados do artigo : {link}: {e}')

        extracted_data.append(article_data)

    # Convertendo data para JSON
    json_data = json.dumps(extracted_data, indent=4)

    # Json de retorno
    return json_data       

