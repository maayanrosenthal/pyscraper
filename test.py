# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

def getTitles(url_test):
    page = urllib2.urlopen(url_test)
    response = page.read()
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find_all(class_='title') # class_ ot scrape by... change to relevant class name / flag
    for x in table:
        print x.get_text('div') # enter tag to scrape

def main():
    url_test = "http://www.fuelchoicessummit.com/Companies/IsraeliCompanies.aspx" # change to requested URL
    getTitles(url_test)

if __name__ == "__main__":
    main()
    print "Done!"
