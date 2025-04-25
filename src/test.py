import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.csdn.net/")

soup = BeautifulSoup(r.text, "html.parser")
contebt