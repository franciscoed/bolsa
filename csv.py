#!/usr/bin/env python

#	Author: Chico
#	Version: 0.1.0
#
#
#
import sys;
import csv;
import urllib2;

def downloadCSV (stock):
    url = 'http://www.google.com/finance/historical?q=' + GOOG + '&histperiod=daily&startdate=Aug+8+2015&enddate=Aug+8+2016&output=csv'
    response = urllib2.urlopen(url)
    return response


def openCsv (stock_name):
    csvReader = csv.reader(stock_name)
    return csvReader
    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(( (s[n] - sma) * multiplier) + sma)

    #now calculate the rest of the values
    for i in s[n+1:]:
        tmp = ( (i - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)

    return ema



def main():

        print (downloadCSV('rent3'))

if __name__ == '__main__':
	sys.exit(main())
