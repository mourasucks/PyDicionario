import requests
import os
from bs4 import BeautifulSoup

class wrapper:
  class Infopedia:
    def search(self,word,lang):
     if lang == "portugues":
      main_url = "https://www.infopedia.pt/dicionarios/lingua-portuguesa"
      params = word
      resp = requests.get(f'{main_url}/{params}')
      soup = BeautifulSoup(resp.text, 'html.parser')
      definicao = soup.find('div', {"class" : "QuadroDefinicao"})
      rows  = definicao.find('div', {"class":"dolDivisaoCatgram"})
      print(rows.get_text())
     if lang == "alemao":
      main_url = "https://www.infopedia.pt/dicionarios/alemao-portugues"
      params = word
      resp = requests.get(f'{main_url}/{params}')
      soup = BeautifulSoup(resp.text, 'html.parser')
      definicao = soup.find('div', {"class" : "QuadroDefinicao"})
      rows  = definicao.find('div', {"class":"dolDivisaoCatgram"})
      print(rows.get_text())
     if lang == "ingles":
      main_url = "https://www.infopedia.pt/dicionarios/ingles-portugues"
      params = word
      resp = requests.get(f'{main_url}/{params}')
      soup = BeautifulSoup(resp.text, 'html.parser')
      definicao = soup.find('div', {"class" : "QuadroDefinicao"})
      rows  = definicao.find('div', {"class":"dolDivisaoCatgram"})
      print(rows.get_text())
     if lang == "frances":
      main_url = "https://www.infopedia.pt/dicionarios/frances-portugues"
      params = word
      resp = requests.get(f'{main_url}/{params}')
      soup = BeautifulSoup(resp.text, 'html.parser')
      definicao = soup.find('div', {"class" : "QuadroDefinicao"})
      rows  = definicao.find('div', {"class":"dolDivisaoCatgram"})
      print(rows.get_text())

api = wrapper.Infopedia()

# função leva 2 argumentos, palavra a pesquisar e linguagem da palavra

api.search("hallo","alemao")