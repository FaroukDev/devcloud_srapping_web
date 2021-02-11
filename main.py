from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-22/'

page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
#results = table.find_all('tr')

for i in range(0,5):
#print('Number of results', title[0])
    title_slice = title[i].text
    print(title_slice[0:-8])








