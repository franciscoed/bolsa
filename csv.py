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
    #url = 'http://www.google.com/finance/historical?q=' + stock + '&histperiod=daily&startdate=Aug+8+2015&enddate=Aug+8+2016&output=csv'
    url = 'http://www.google.com/finance/historical?q=' + urllib2.quote('rent3') + '&histperiod=' + urllib2.quote('daily') + \
    '&startdate=' + urllib2.quote('Aug+8+2015') + '&enddate=' + urllib2.quote('Aug+8+2016') + '&output=csv'

    #quotedUrl = urllib.quote(url, ':/?=&+')
    print(url)
    try:
        response = urllib2.urlopen(url).read()
    except Exception as e:
        print(e)
        raise e
    return response

def openCsv (stock_name):
    csvReader = csv.reader(stock_name)
    return csvReader

def closeList (csv):
    tempList = []
    for row in csv:
        if csv.line_num == 1:
            continue
        tempList.append(row[4])
    tempList.reverse()
    return tempList


def main():

        csvFile = downloadCSV('rent3')
        #csvOpenFile = openCsv(csvFile)
        #print(closeList(csvOpenFile))

if __name__ == '__main__':
	sys.exit(main())
