from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#url of scrapping debut du script
urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-30/'

#on request la page avec urllib
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

#scrap element a in xbox page
title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
#results = table.find_all('tr')

#for loop in element a of xbox page
for i in range(0,5):
#print('Number of results', title[0])
    title_slice = title[i].text
    print(title_slice[0:-8])













