# API de sinônimos (PT-BR)

API para obter os sinônimos de uma palavra em português.

Acesse [aqui](https://api-synonyms.herokuapp.com/).

## Sobre

Como não há/não foi encontrado um banco de dados público com essas informações, os sinônimos são obtidos por *web scraping* do site [sinonimos.com.br](https://www.sinonimos.com.br). Como a realização do *request* pode demorar, na primeira vez que uma palavra é pesquisada, a API salva essa na sua base de dados, para futuras consultas.

## Utilização

Para a obtenção de um sinônimo, utilize a rota a seguir, passando a palavra desejada. Por limitações do site em que estamos retirando os dados, a palavra deve ser passada sem acentuação.

```
api/v1/resources/synonym?word=PALAVRA
```

### Exemplo

Para obtenção dos sinônimos da palavra **garrafa**:

**Request URL**:
```
https://api-synonyms.herokuapp.com/api/v1/resources/synonym?word=garrafa
```
**Response Body**:
```
{
    "_id": "62f40dc7bf20858b4b8593b7",
    "syn": [
        [
            "casco",
            "vidro"
        ],
        [
            "botelha",
            "frasco",
            "jarra"
        ]
    ],
    "word": "garrafa"
}
```
No exemplo acima, cada elemento do vetor *syn* corresponde aos sinônimos de um significado da palavra. No arquivo [web_scraping.py](utils/web_scrapping.py), está comentado uma parte do código que traz qual o significado do vetor dos sinônimos, caso necessário.

## Tecnologias Utilizadas

As seguintes ferramentas foram usadas na construção do projeto:
- Python
- Flask
- BeautifulSoup
- MongoDB
- Entre outras...

## Desenvolvedora

Feito com 🖤 por Alice Ribeiro 

[![Linkedin Badge](https://img.shields.io/badge/-Alice-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/alice-ribeiro-280812182/)](https://www.linkedin.com/in/alice-ribeiro-280812182/) 
[![Gmail Badge](https://img.shields.io/badge/-ciceribeiroo@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ciceribeiroo@gmail.com)](mailto:ciceribeiroo@gmail.com)

### Vamos fazer algo louco juntos?
