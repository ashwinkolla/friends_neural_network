#get libraries request and BeatifulSoup4
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from web_funcs import * #get webscrape functions 
import csv


webpage_html = get_url('https://fangj.github.io/friends/season/0101.html')

soup = BeautifulSoup(webpage_html, 'html.parser')


dialogue = soup.find_all('font')

person_quotes = {}

#clean text 
for font in dialogue[3:]:
    temp = font.text
    if ":" in temp:
        if temp.count("[") == 0:
            temp = temp.replace(u'\xa0', '')
            temp = temp.replace('\n', ' ')
            temp = temp.split(":")
            person_quotes[temp[0]] = person_quotes.get(temp[0],[]) + [temp[1]]


