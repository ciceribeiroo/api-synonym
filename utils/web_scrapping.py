import requests
from bs4 import BeautifulSoup
from models.word import word_class

url = "https://www.sinonimos.com.br/"

def get_synonyms(word):
    res = requests.get(url+word)
    soup = BeautifulSoup(res.text, 'html.parser')
    # the element with content-wrap class only exists when the word exists
    if soup.find(class_="content-wrap") is not None:
        syns_list = find_syn(soup)
        return word_class(word, syns_list)

def find_syn(soup):
    syns = soup.findAll(class_="s-wrapper")
    syns_list = []
    for i in syns:
      syns_el = i.findAll(class_="sinonimo")
      # if elements with sinonimo class does't exist, look for span elements that aren't the example one
      if len(syns_el)==0:
        span = i.findAll("span")
        syns_el = [el for el in span if "Exemplo" not in el.text]
      syns_text = [el.text for el in syns_el]
      syns_list.append(syns_text)
      #meaning_el = i.find(class_="sentido") 
      # if elements with sentido class doesn't exist, the element doesn't exist
      # if meaning_el is not None:
      #   meaning = meaning_el.text.replace(":", "")
      #   number = i.find(class_="number").text
      #   syns_list.append([number, meaning, syns_text])
      # else:
      #   number = i.find(class_="number").text
      #   syns_list.append([number, syns_text])
    return syns_list