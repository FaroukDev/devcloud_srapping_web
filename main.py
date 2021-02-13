import logging
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

logging.info('script start')
logging.info('Scrapping element of xbox one page with class from url link jeux videos.com')

def getXBox():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-30/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    logging.info('fetch element in for loop')
    games_dict = {}
    for i in range(0,5):
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getXBox())

logging.info('scrapping element title ps5 in page jeux videos.com ')
def getPs5():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-22/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    games_dict = {}
    for i in range(0,5):
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getPs5())

logging.info('scrapping element title pc in page jeux videos.com ')
def getPc():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-10/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    games_dict = {}
    for i in range(0,5):
        title_slice = title[i].text
        title_slice = title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getPc())

logging.info("end of script")

  

    













