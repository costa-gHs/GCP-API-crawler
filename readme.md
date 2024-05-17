# API de Extração de Artigos CNN

Esta API foi desenvolvida usando Google Cloud Functions e a biblioteca BeautifulSoup em Python. Ela extrai dados de artigos do site da CNN Brasil, incluindo o título, subtítulo e autor do artigo.

## URL da API
https://southamerica-east1-hip-orbit-422421-j5.cloudfunctions.net/cnn-extractor-articles

## Autenticação
A API exige um Bearer Token para autenticação. Utilize o token fornecido ao fazer as requisições.

```
token : eyJhbGciOiJSUzI1NiIsImtpZCI6IjMyM2IyMTRhZTY5NzVhMGYwMzRlYTc3MzU0ZGMwYzI1ZDAzNjQyZGMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiNjE4MTA0NzA4MDU0LTlyOXMxYzRhbGczNmVybGl1Y2hvOXQ1Mm4zMm42ZGdxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTEwMTMzNDA3NTk4Njg5NTc5NjQ2IiwiZW1haWwiOiJoZW5yaXF1ZWRlbGxpMjAxM0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IjZtZFppc0ViUHpoNEpjQkFObFIwMlEiLCJuYmYiOjE3MTU5Njk2NTAsImlhdCI6MTcxNTk2OTk1MCwiZXhwIjoxNzE1OTczNTUwLCJqdGkiOiIwOTkwYTYyMWJkZmI3ZWJmY2JhZTQ0MzEwM2I3OTBiYWM5ZmQwOTViIn0.qAtCDWsvSCKusuNlhxRfMLcj9bzhRHQq1m60NpD8zAncP4o64fb3_-G7Uxm4FiQHYiLnI0xdJeH4Hj0OIMivxeck-JCKR9s5tiZLwXjhK7vySuoc--8I-qjUb6jUE6E3b06a8t4hoBqlBnABMc7OJlyoi4VnJ4fPKxPVpoQVLlImYyQczxb-m5r8nJQekgZ5Im8rvY-s0Bh3aAjp6qRDW34-s2qG_ngFnOHSnr5dSCx6Bx-l9LA9Q48lIz1v5858bAqF0j8MfQK7dLpSitjfWm9ZWlM0JK3HMAjxYFk_kwFt9BXRxRo6wTpNP72NFyzGNoGfFG7xabz04uzb-anC5Q
```

## Tempo de Timeout
O tempo limite (timeout) mínimo para requisições à API é de 60.000 ms (60 segundos).

## Parâmetros
A API requer um parâmetro JSON no corpo da requisição (body), conforme o exemplo abaixo:

```json
{
    "termo_pesquisa": "OpenAI"
}
```
## Retorno
A API solicitada ira retornar os dados extraidos em formato Json, conforme o exemplo abaixo:

```json
{
    "data":
    {
        "title": "Cofundador da OpenAI deixa empresa criadora do ChatGPT",
        "subtitle": "Ilya Sutskever afirmou que est\u00e1 trabalhando em um novo projeto",
        "author": "da Reuters"
    },
    "data" :
    {
        "title": "OpenAI usar\u00e1 conte\u00fado do Financial Times para embasar intelig\u00eancia artificial",
        "subtitle": "Com nova parceria, ChatGPT responder\u00e1 usu\u00e1rios com informa\u00e7\u00f5es, resumos, cita\u00e7\u00f5es e links da produ\u00e7\u00e3o feita pelo jornal",
        "author": "Angela Christy"
    },
}
```

## Observações
Gostaria de ter implementado a inserção no Cloud Storage, para exibir no BigQuery, porem houve alguns problemas :
- Problema de autenticação, que foi resolvido com o Bearer Token, porém não em tempo de inserir logica de tablea;
- Problema de Time-out :
	- Feita extração de multiplas notícias, com um request para cada href da noticia;
	- Isso gera uma "demora" no retorno da API, pode ser aprimorado, porem não houve tempo habil;