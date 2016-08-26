#!/usr/bin/env python

#	Author: Chico
#	Version: 0.1.0
#
#
#
import sys;
import csv;
from datetime import datetime;


def getList ():
    #lista = ('rent3', 'klbn4', 'abev3', 'bvmf3', 'embr3', 'hype3')
    lista = ('hype3',)
    return lista

def downloadCSV ():
    # Code Fount at: http://www.theodor.io/scraping-google-finance-data-using-pandas/
    # Specify Date Range
    start = datetime(2015, 8, 1)
    end = datetime.today()

    # Specify symbol
    symbol = 'rent3'

    aapl_from_google = web.DataReader("%s" % symbol, 'google', start, end)

    aapl_from_google.to_csv('%s.csv' % symbol)


def openCsv (stock_name):
    csvFile = open('sampleCSV/' + stock_name + '.csv')
    csvReader = csv.reader(csvFile)
    return csvReader

def closeList (csv):
    tempList = []
    for row in csv:
        if csv.line_num == 1:
            continue
        tempList.append(round(float(row[4]),2))
    tempList.reverse()
    return tempList




def sma(s, n):

    sma = []
    dp = []
    upper = []
    lower = []
    bandwidth = []
    j = 0
    for i in s[n-1:]:
        tmp = sum(s[j:j+n])/n
        dptmp = pstdev(s[j:j+n])
        uppertmp = round(tmp + (dptmp*2),2)
        lowertmp = round(tmp - (dptmp*2),2)
        j = j+1
        sma.append(round(tmp,2))
        dp.append(round(dptmp,2))
        upper.append(round(uppertmp,2))
        lower.append(round(lowertmp,2))
        bandwidth.append(round(uppertmp - lowertmp,2))
    print sma

    return sma

def mean(data):
    #Function from: http://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    #Function from: http://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    #Function from: http://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5



def main():
    stockList = getList()
    for i in range(len(stockList)):
        csvReader = openCsv(stockList[i])
        ListValues = closeList(csvReader)
        smaValues = sma(ListValues, 20)



if __name__ == '__main__':
	sys.exit(main())
