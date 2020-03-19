#!/usr/bin/python

import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://lenta.ru/')
html = BS(r.content,'html.parser')



for el in html.select('.item.article'):
	title = el.select('rightcol')
	print(title[0].text)