from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

def getXBox():
    #url of scrapping debut du script
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-30/'

    #on request la page avec urllib
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())

    #scrap element a in xbox page
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    #results = table.find_all('tr')

    games_dict = {}
    #for loop in element a of xbox page
    for i in range(0,5):
    #print('Number of results', title[0])
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getXBox())
def getPs5():
    #url of scrapping debut du script
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-22/'

    #on request la page avec urllib
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())

    #scrap element a in xbox page
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    #results = table.find_all('tr')

    games_dict = {}
    #for loop in element a of xbox page
    for i in range(0,5):
    #print('Number of results', title[0])
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getPs5())

def getPc():
    #url of scrapping debut du script
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-10/'

    #on request la page avec urllib
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup.prettify())

    #scrap element a in xbox page
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    #results = table.find_all('tr')

    games_dict = {}
    #for loop in element a of xbox page
    for i in range(0,5):
    #print('Number of results', title[0])
        title_slice = title[i].text
        title_slice = title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return games_dict

print(getPc())

  

    













