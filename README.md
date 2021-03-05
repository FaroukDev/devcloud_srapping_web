The project consists to scrap data from jeuxvideos.com on different url.


![alt text](https://user-images.githubusercontent.com/43003646/110116550-efc3b600-7db7-11eb-9b39-24bb6005dcea.gif)

## Installation

Here are the dependencies to install in the project

```bash
pip install beautifulsoup4
pip install Flask
pip install flask_mysql_connector
pip install urllib3
pip install mysql-connector
pip install Flask-Cors
pip install smtplib
```

## Usage

```
run the script with python3 app.py
```

```python
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


```


