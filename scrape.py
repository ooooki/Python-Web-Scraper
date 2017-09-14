from bs4 import BeautifulSoup
import requests,sys

#you can also get the twitter handle from user
handle = ' ' 
res = requests.get('https://www.google.com/')
soup = BeautifulSoup(res.text,'lxml')
print(res)
print("$$$")
print(soup)



