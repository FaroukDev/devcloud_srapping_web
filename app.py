import logging
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
import mysql.connector
import logging
#j'importe les fonction du fichier script.py
from flask import Flask, request, render_template,jsonify
from flask_mysql_connector import MySQL
#https://flask-cors.readthedocs.io/en/latest/
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(
    filename='test.log', 
    level=logging.DEBUG,format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')
logging.info('script start')
logging.info('Scrapping element of xbox one page with class from url link jeux videos.com')

app = Flask(__name__)
CORS(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'delpiero92'
app.config['MYSQL_HOST'] = 'ms1'
app.config['MYSQL_DATABASE'] = 'video_game'

mysql = MySQL(app)


@app.route('/')
def index():
    return 'hello world'

@app.route('/get_xbox')
def getXBox():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-30/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    logging.info('fetch element in for loop')
    games_dict = {}
    for i in range(0,10):
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return jsonify(games_dict) 

#print(getXBox())

logging.info('scrapping element ps5 title in page jeux videos.com ')

@app.route('/get_ps5')
def getPs5():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-22/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    games_dict = {}
    for i in range(0,10):
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return jsonify(games_dict)


logging.info('scrapping element pc title in page jeux videos.com ')
@app.route('/get_pc')
def getPc():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-10/'
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    games_dict = {}
    for i in range(0,10):
        title_slice = title[i].text
        title_slice = title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return jsonify(games_dict)

#print(getPc())

logging.info("end of script")

  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
    













