"""
library for fetching live data from yahoo


"""

import requests
from bs4 import BeautifulSoup, NavigableString
import locale
import re


# locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
# konverze do floatu... locale.atof('1,000,000.53')


def getStocks(stocks: list) -> dict:
    """get list of nasdaq stock"""
    rsDa = {}
    for ii in stocks:
        rsDa[ii] = getStock(stock=ii)
    return rsDa


def getStock(stock: str) -> dict:
    """get nasdaq stock"""
    r = requests.get(f"https://finance.yahoo.com/quote/AMZN?p={stock}&.tsrc=fin-srch").text
    soup = BeautifulSoup(r, 'html.parser')
    alldata = soup.find_all('tbody')
    ydata = {}

    def getLast(tag):
        for ii in tag.children:
            if isinstance(ii, NavigableString):
                return ii
            else:
                return getLast(ii)

    for tables in alldata:
        for items in tables.find_all('tr'):
            name = items.find_all("td")[0]
            value = getLast(items.find_all("td")[1])
            valRes = re.match("^[\d\,]+\.*\d+$", value)
            if valRes != None:
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
                ffR = locale.atof(value)
                ydata[name.text] = ffR
            else:
                ydata[name.text] = value

    return ydata
