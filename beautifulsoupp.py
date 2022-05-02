#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 00:47:31 2022

@author: morganstump
"""

#output file is the HTML content
#console shows everything else

from bs4 import BeautifulSoup as bs
import requests
import nltk

#lnkk to website
url = "https://declaration.fas.harvard.edu/resources/text"
response = requests.get(url)

#printint this will print the HTML content of the page
html = response.content 

#prints in HTML format
soup = bs(html, "lxml")
#print(soup)

#<title></title>
print("\nThe title of the page is: \n", soup.title)

print("\nThe title of the page without the element is: ", soup.title.get_text())

#pulls from HTMP code <h1></h1?
print("\nThe first header is: ", soup.h1)

#prints the text of the header
print("\nThe first header without the element is: ", soup.h1.get_text())

print("\nThe elements attribute is: ", soup.a["href"])

#if says 200, downloaded successfully
print("Status is complete if 200 is displayed: ", response.status_code)

#in order to parse, must create an instance of bs
soup = bs(response.content, 'html.parser')
#this retrieves all text related to the p tag
print(soup.find_all('p')[0].get_text())

#to format the HTML content nicely, you prettify()
#print SOUP console in output file
with open("output_text.txt", "w") as f:
    print(soup.prettify(),file=f)
    
#view 10 most used words in console
print()
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
print(freq.most_common(100))
print()


response.close()