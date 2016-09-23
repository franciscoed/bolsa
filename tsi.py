#!/usr/bin/env python

#	Author: Chico
#	Version: 0.1.0
#
#
#
import sys;
import csv;
#import pandas as pd;
from datetime import datetime;
#import pandas_datareader.data as web;

def getList ():
    #lista = ('rent3', 'klbn4', 'abev3', 'bvmf3', 'embr3', 'hype3')
    lista = ('vale5',)
    return lista

def downloadCSV ():
    # Code Fount at: http://www.theodor.io/scraping-google-finance-data-using-pandas/
    # Specify Date Range
    start = datetime(2015, 8, 1)
    end = datetime.today()

    # Specify symbol
    symbol = 'rent3'

    #aapl_from_google = web.DataReader("%s" % symbol, 'google', start, end)

    #aapl_from_google.to_csv('%s.csv' % symbol)


def openCsv (stock_name):
    csvFile = open('sampleCSV/' + stock_name + '.csv')
    csvReader = csv.reader(csvFile)
    return csvReader

def closeList (csv):
    tempList = []
    for row in csv:
        if csv.line_num == 1:
            continue
        tempList.append(row[4])
    tempList.reverse()
    return tempList

def momentum (closeList):
    momentumList = []
    for i in range(len(closeList)):
        if i == 0:
            continue
        momentumList.append(round(float(closeList[i])-float(closeList[i-1]),2))
    return momentumList

def momentumAbs (closeList):
    momentumAbsList = []
    for i in range(len(closeList)):
        if i == 0:
            continue
        momentumAbsList.append(abs(round(float(closeList[i])-float(closeList[i-1]),2)))
    return momentumAbsList


def ema(s, n):
    """
    Function found at http://stackoverflow.com/questions/488670/calculate-exponential-moving-average-in-python

    returns an n period exponential moving average for
    the time series s

    s is a list ordered from oldest (index 0) to most
    recent (index -1)
    n is an integer

    returns a numeric array of the exponential
    moving average
    """
    #s = array(s)
    ema = []
    j = 1

    #get n sma first and calculate the next n period ema
    sma = sum(s[:n]) / n
    multiplier = 2 / float(1 + n)
    ema.append(sma)

    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(( (s[n] - sma) * multiplier) + sma)

    #now calculate the rest of the values
    for i in s[n+1:]:
        tmp = ( (i - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)

    return ema

def emapandas(s, n):
    data = { 'stock' : s}
    df = pd.DataFrame(data)
    emapandas = df.ewm(span=25).mean()
    return emapandas

def tsi (emaList, emaAbsList):
    tsiList = []
    for i in range(len(emaList)):
        tsiList.append(100*(emaList[i]/emaAbsList[i]))
    return tsiList


def main():
    stockList = getList()
    for i in range(len(stockList)):
        csvReader = openCsv(stockList[i])
        ListValues = closeList(csvReader)

        momentumValues = momentum(ListValues)
	momentumAbsValues = momentumAbs(ListValues)

        ema25Momentum = ema(momentumValues,25)
        ema13ema25 = ema(ema25Momentum,13)
        ema25MomentumAbs = ema(momentumAbsValues,25)
        ema13ema25Abs = ema(ema25MomentumAbs,13)

        tsiList = tsi(ema13ema25, ema13ema25Abs)
        tsi7List = ema(tsiList, 7)
	print tsiList
        if tsiList[-1] > tsi7List[-1] and tsiList[-1] > 0:
            print (stockList[i] + ': ' + 'Compra')
        elif tsiList[-1] < tsi7List[-1] and tsi7List < 0:
            print (stockList[i] + ': ' + 'Vende')
        else:
            print (stockList[i] + ': ' + 'Faz nada')

        downloadCSV()

if __name__ == '__main__':
	sys.exit(main())
