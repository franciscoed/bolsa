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
    lista = ('rent3', 'klbn4', 'abev3', 'bvmf3', 'embr3', 'hype3')
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
        tempList.append(row[4])
    tempList.reverse()
    return tempList




def sma(s, n):

    sma = []

    #get n sma first and calculate the next n period ema
    tmp = sum(s[:n]) / n
    sma.append(tmp)

    #now calculate the rest of the values
    for i in s[n+1:]:
        tmp = sum(s[i:i+n])
        ema.append(tmp)

    return sma



def main():
    stockList = getList()
    for i in range(len(stockList)):
        csvReader = openCsv(stockList[i])
        ListValues = closeList(csvReader)
        sma = sma(ListValues, 20)



if __name__ == '__main__':
	sys.exit(main())
