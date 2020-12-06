import urllib.request
import re

def urlToPDF(url):
#need to change so url isn't static and can be pulled everytime a new one is uploaded.
    urllib.request.urlretrieve(url, "C:/Adam's Apps/Covid19DataProject/policywebscraper/Executive Orders/test.txt")
#test urlib vs python default request library for speed and space
