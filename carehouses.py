import sqlite3
import requests
import ssl
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import re

'''Would like three individual categories;
Category 1
Care homes with Nursing

Category 2
Care homes without nursing

Category 3
Other care services'''

#GROUP NAME, HOME NAME, ADDRESS, WEBSITE, NAME OF "PERSON IN CHARGE" AND TITLE, 
#PHONE NUMBER 1, PHONE NUMBER 2 OR MORE PHONE NUMBERS IF POSSBILE TO FIND.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('houses.sqlite')
cur = conn.cursor()

baseurl = "https://www.carehome.co.uk/care_search_results.cfm/searchcountry/England/startpage"

cur.executescript('''
	CREATE TABLE IF NOT EXISTS Houses(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
		 group_id INTEGER, 
		 name TEXT,
		 address TEXT, 
		 website TEXT, 
		 personinch TEXT, 
		 phone1 TEXT,
		 phone2 TEXT, 
		 phone3 TEXT);

	CREATE TABLE IF NOT EXISTS Groups(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE);

	CREATE TABLE IF NOT EXISTS Websites(
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name TEXT UNIQUE)''')

def sopa(tag, url):
	wd = webdriver.Chrome("/WebDriver/bin/chromedriver.exe")
	
	wd.get(url)
	html_page = wd.page_source
	wd.quit()
	
	soup = BeautifulSoup(html_page, "html.parser")

	tags=soup(tag)
	return tags
	
pagina = 1

while True:
	url = baseurl + "/" + str(pagina)
	print("Recuperando...",url)
	
	tags=sopa("a", url)
	
	urltodascasas = re.findall("(https://www.carehome.co.uk/carehome.cfm/searchazref/[0-9A-Z]+)" , str(tags))
	
	for urlcadacasa in urltodascasas:
		print("Entrando en:", urlcadacasa)
		

		tags=sopa("div", urlcadacasa)

		textRegext = re.compile(r'''
		(<li|<h2[a-zA-Z0-9="-]+|<li>[a-zA-Z="<]+"h4")			#proceso li, h2 o h4
		(>[a-zA-Z0-9"'-() ]+<)									#entre los signos mayores
		''', re.VERBOSE | re.DOTALL)
		
		nombre = textRegext.findall(str(tags))
		for cada_nombre in nombre:
			try:
				print(cada_nombre[1])
			except IndexError:

				print("No encuentro indice 1")

				continue

	pagina += 1
	conn.commit()