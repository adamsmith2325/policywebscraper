from convert import *
from fileimport import *
from readin import *

def pdfToTxt(url):
   txtFile = urlToPDF(url)
   converted = convertFile("C:/Adam's Apps/Covid19DataProject/policywebscraper/Executive Orders/test.txt")
   #keyWordSearch = readin(converted)
   #print(keyWordSearch)

#Test
pdfToTxt('https://www2.illinois.gov/sites/gov/Documents/CoronavirusDisasterProc-9-18-2020.pdf')