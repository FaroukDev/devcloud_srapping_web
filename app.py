#!/usr/bin/env python
from datetime import datetime
print(datetime.now())
import logging
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
import mysql.connector
import logging
from flask import Flask, request, render_template,jsonify,json
from flask_mysql_connector import MySQL
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import time


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

logging.info("end of script")


def send_email(games):
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
        jsonify(games_dict)
    from_gmail_user = "extramilessimplon@gmail.com"
    to_gmail_user = "extramilessimplon@gmail.com"
    gmail_password = "delpiero92"

    msg = MIMEMultipart()
    body = MIMEText("Voici les derniers jeux" + games_dict)
    msg.attach(body)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(from_gmail_user, gmail_password)
        server.sendmail(from_gmail_user, to_gmail_user,msg.as_string())
        server.close()
        print("email sent !")
    except Exception as e:
        print("Email not sent")
        print(e)

def scrapperGames():
    urlpage = 'https://www.jeuxvideo.com/meilleurs/machine-22/'
    cron = time.strftime('%Y-%-m-%-d')
    file_name = cron + ".txt"
    output = open(file_name, "w")
    webpage = urllib.request.urlopen(urlpage).read().decode('utf-8')
    soup = BeautifulSoup(webpage, 'html.parser')
    title = soup.find_all('a', attrs={'class': 'gameTitleLink__196nPy'})
    webpage = re.sub( r'<[^>]*>', ' ', webpage ).strip()
    games_dict = {}
    for i in range(0,10):
        title_slice = title[i].text
        title_slice[0:-8]
        title_slice = title_slice.replace("'"," ")
        games_dict.update({i+1:title_slice})
    return output.write(json.dumps(games_dict))

scrapperGames()
    

print("Ok done !")
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
    













