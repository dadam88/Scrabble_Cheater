import requests 
from bs4 import BeautifulSoup

def define(word):
	url = "http://www.dictionary.reference.com/browse/{todefine}?s=t".format(todefine=word)
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	define = soup.find("div", {"class": "def-content"})
	return define.text.encode('utf-8')