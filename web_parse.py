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

dialogue_clean = []

#clean text 
for font in dialogue[3:]:
    temp = font.text
    if ":" in temp:
        if temp.count("[") == 0:
            temp = temp.replace(u'\xa0', '')
            temp = temp.replace('\n', ' ')
            temp = temp.split(":")
            if temp not in dialogue_clean:
                dialogue_clean.append(temp)

#for k in dialogue_clean:
 #   print(k)

with open("friends.csv", "w") as friends:
    writer = csv.writer(friends, delimiter=',')
    for lines in dialogue_clean:
        writer.writerow([lines[0] + lines[1]])                                                                          

     
