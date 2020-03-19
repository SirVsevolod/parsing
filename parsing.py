#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/fryazino?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'
,'accept':'*/*'}
HOST = 'https://www.avito.ru'


def get_html(url,params = None):
	r = requests.get(url, headers = HEADERS, params = params)
	return r



def get_content(html):
	soup = BeautifulSoup(html,'html.parser')
	items = soup.find_all('div',class_='snippet-horizontal')
	#print(items)

	cars = []

	for item in items:

		price = item.find('span',class_='snippet-price')
		street = item.find('span',class_='item-address__string')

		if price:
			price = price.get_text(strip = True)
		else:
			price = 'Цену уточняйте'

		if street:
			street = street.get_text(strip = True)
		else:
			street = 'Адресс уточняйте'


		cars.append({
			'title': item.find('a',class_='snippet-link').get_text(strip = True),
			'link': HOST + item.find('a',class_='snippet-link').get('href'),
			'price':price,
			'street': street
			})
	print(cars)



def parse():
	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
	else:
		print("Error")

parse()