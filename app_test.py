import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
import importlib
from app import getPc,getXBox,getPc

class TestMyAPP(unittest.TestCase):
    bs = None
    def test_pc(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-10/'
        TestMyAPP.bs = BeautifulSoup(urlopen(url), 'html.parser')

    def test_description_pc(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-10/'
        soup = BeautifulSoup(url, "html.parser")
        content = soup.findAll('a',{'class': 'gameTitleLink__196nPy'})
        self.assertIsNotNone(content)
        
    def test_ps5(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-22/'
        TestMyAPP.bs = BeautifulSoup(urlopen(url), 'html.parser')

    def test_description_p5(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-22/'
        soup = BeautifulSoup(url, "html.parser")
        content = soup.findAll('a',{'class': 'gameTitleLink__196nPy'})
        self.assertIsNotNone(content)

    def test_xbox(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-30/'
        TestMyAPP.bs = BeautifulSoup(urlopen(url), 'html.parser')

    def test_description_xbox(self):
        url = 'https://www.jeuxvideo.com/meilleurs/machine-30/'
        soup = BeautifulSoup(url, "html.parser")
        content = soup.findAll('a',{'class': 'gameTitleLink__196nPy'})
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()