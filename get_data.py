import sqlite3
import requests
import ssl
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('houses.sqlite')
cur = conn.cursor()

baseurl = "https://www.carehome.co.uk/care_search_results.cfm/searchcountry/England/startpage"

cur.execute('SELECT name FROM Websites')
websites = cur.fetchall()

'''group_id INTEGER, 
		 name TEXT,
		 address TEXT, 
		 website TEXT, 
		 personinch TEXT, 
		 phone1 TEXT,
		 phone2 TEXT, 
		 phone3 TEXT);'''

for site in websites:
	url = site[0]
	print("Recuperando...",url)
	
	wd = webdriver.Chrome("/WebDriver/bin/chromedriver.exe")
	wd.get(url)
	html_page = wd.page_source
	wd.quit()
	
	soup = BeautifulSoup(html_page, "html.parser")

	tags=soup("div")
	
	
	nombre = re.findall("<span>(.+)</span>" , str(tags))
	try:
		print(nombre[3])
	except:
		continue

	
	# for urlcadacasa in urltodascasas:
	# 	cur.execute('''INSERT OR IGNORE INTO Websites (name) 
	# 		VALUES ( ? )''', (urlcadacasa,))
	# pagina += 1
	# conn.commit()
