import time
import sys
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import md5
import ConfigParser
from itertools import count
import pdb

config = ConfigParser.ConfigParser()
config.read('supreme_items.cfg')
# grail = config.get('grail', 'keyword')
# grail_color = config.get('grail', 'color')
# size = config.get('grail', 'size')
# catagory = config.get('grail', 'catagory')
products = 1
name_field = config.get('info', 'name')
email_field = config.get('info', 'email')
phone_number = config.get('info', 'phone')
address_field = config.get('info', 'address')
zip_field = config.get('info', 'zip')
state_field = config.get('info', 'state')
country_field = config.get('info', 'country')
city_field = config.get('info', 'city')

credit_card_number = config.get('credit card', 'ccnum')
credit_card_month = config.get('credit card', 'ccmonth')
credit_card_year = config.get('credit card', 'ccyear')
cvc = config.get('credit card', 'cvc')

mainUrl = "http://www.supremenewyork.com/shop/all/" 
baseUrl = "http://supremenewyork.com"
checkoutUrl = "https://www.supremenewyork.com/checkout"




browser = Browser('chrome')


try:
	input('Enter google Info.')
except SyntaxError:
	pass
try:
    browser.visit(baseUrl)
    input('Press enter to cop')

except SyntaxError:
	pass

start_time = time.time()

def main():
	if grail in thing_one:
		print('Found item!')
		html_soup(thing_one)
	else:
		print(thing_one)
		print('product not found.')

def html_soup(thing_one):
    soup = BeautifulSoup(thing_one, "html.parser")
    for div in soup.find_all('div', { "class" : "inner-article" }):
        product = ""
        color = ""
        link = ""
        for a in div.find_all('a', href=True, text=True):
            link = a['href']
        for a in div.find_all(['h1','p']):
            if(a.name=='h1'):
                product = a.text
            elif(a.name=='p'):
                color = a.text
                
        product_exist(link,product,color)

def product_exist(product_link, product_name, product_color):
	if (grail in product_name and grail_color == product_color):
		product_url = baseUrl + product_link
		print('\nFound grail! \n')
		print('Name: '+product_name+'\n')
		print('Color: '+product_color+'\n')
		print('URL: '+product_url+'\n')
		print('starting to cop.....')
		buy_grail(product_url)

def  buy_grail(u):
	browser.visit(u)
	browser.find_option_by_text(size).first.click()
	browser.find_by_name('commit').click()
	if browser.is_text_present('item'):
		print('Added to cart!')
	print('Now checking out....')
	
def checkout():	
	
	time.sleep(.1)
	
	browser.visit(checkoutUrl)
	print('Entering your info')
	
	time.sleep(.1)
	
	browser.fill('order[billing_name]', name_field)
	browser.fill('order[email]', email_field)
	browser.fill('order[tel]', phone_number)
	
	time.sleep(.2)
	
	browser.fill('order[billing_address]', address_field)
	browser.fill('order[billing_zip]', zip_field)
	browser.fill('order[billing_city]', city_field)
	browser.select('order[billing_state]', state_field)
	browser.select('order[billing_country]', country_field)
	
	time.sleep(.3)
	
	browser.fill('credit_card[nlb]', credit_card_number)
	browser.select('credit_card[month]', credit_card_month)
	browser.select('credit_card[year]', credit_card_year)
	browser.fill('credit_card[rvv]', cvc)
	
	time.sleep(.1)

	browser.find_by_css('.terms').click()
	
	time.sleep(2)

	browser.find_by_name('commit').click()

	print('COP TIME: %s' % (time.time() - start_time))

	quit()	



for i in range(products):
	grail = config.get('grail%d' % i, 'keyword')
	grail_color = config.get('grail%d' % i, 'color')
	size = config.get('grail%d' % i, 'size')
	catagory = config.get('grail%d' % i, 'catagory')
	thing_one = requests.get(mainUrl+catagory).text
	main()


# i = 1
# while (True):
# 	print('Attempt Number:' + str(i))
# 	main()
# 	i += 1
# 	time.sleep(.1)


checkout()