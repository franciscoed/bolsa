from __future__ import print_function

import json
import boto3
import csv
import urllib2


print('Loading function')

s3 = boto3.client('s3')



def downloadCSV (stock):
    #url = 'http://www.google.com/finance/historical?q=' + stock + '&histperiod=daily&startdate=Aug+8+2015&enddate=Aug+8+2016&output=csv'
    url = 'http://www.google.com/finance/historical?q=' + urllib2.quote('rent3') + '&histperiod=' + urllib2.quote('daily') + \
    '&startdate=' + urllib2.quote('Aug+8+2015') + '&enddate=' + urllib2.quote('Aug+8+2016') + '&output=' + urllib2.quote('csv')

    req = urllib2.Request(url)
    print(url)
    try:
        response = urllib2.urlopen(req)
    except Exception as e:
        print(e)
        raise e
    return response


def lambda_handler(event, context):
    bucket = 'chicolambdatest'
    key = 'rent3'
    csv=downloadCSV(key)

    try:
        #response = s3.put_object(Bucket=bucket, Key=key, Body=csv)
        print('upload ok')
        print(csv)
        #return response

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
