import yfinance as yf
import datetime
import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests




def getHistoryDataForTicker(ticker):
    """get all historical data (daily) for ticker
    @:return DataFrame with history data
    """
    msft = yf.Ticker(ticker)
    hist = msft.history(interval="1d",
                        start=datetime.datetime.strptime("2001-01-01","%Y-%M-%d"))
    return hist

def getUpDownForTicker(ticker):
    msft = yf.Ticker(ticker)
    dhh = msft.history(interval="1d",
                        start=datetime.datetime.strptime("2001-01-01", "%Y-%M-%d"))
    dhh['diff_hl']=((dhh['High']-dhh['Low'])/2)+dhh['Low']
    aa=[]
    yesterday=0
    for (index, series) in dhh.iterrows():
        today = series['diff_hl']
        if today>=yesterday:
            aa.append('up')
        else:
            aa.append('down')
        yesterday=today
    dhh['smer']=aa
    thh=dhh.loc[:,['smer']]
    return thh


def getSP500Tickers():
    """getSP500 tickers"""
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    tickers = [s.replace('\n', '') for s in tickers]
    return tickers



# tickers=getSP500Tickers()
# start = datetime.datetime(2019,1,1)
# end = datetime.datetime(2019,7,17)
# data = yf.download(tickers, start=start, end=end)
# print(data)
