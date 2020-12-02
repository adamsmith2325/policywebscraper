import urllib.request
import re

url = 'https://www2.illinois.gov/sites/gov/Documents/CoronavirusDisasterProc-9-18-2020.pdf'
#need to change so url isn't static and can be pulled everytime a new one is uploaded.

urllib.request.urlretrieve(url, 'C:/Covid-19 Data Project/ Executive Orders')
#test urlib vs python default request library for speed and space
