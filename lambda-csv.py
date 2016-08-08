from __future__ import print_function

import json
import boto3
import csv
import urllib2
import urllib


print('Loading function')

s3 = boto3.client('s3')



def downloadCSV (stock):
    url = 'http://www.google.com/finance/historical?q=BVMF%3ARENT3&output=csv'
    #url = 'https://www.google.com/finance/historical?q=rent3&output=csv'
    #url = 'http://www.google.com/finance/historical?q=' + urllib.quote('rent3') + '&histperiod=' + urllib.quote('daily') + \
    #'&startdate=' + urllib.quote('Aug+8+2015') + '&enddate=' + urllib.quote('Aug+8+2016') + '&output=' + urllib.quote('csv')

    print(url)
    try:

        response = urllib2.urlopen(url).read()
        print(response)
    except Exception as e:
        print(e)
        raise e
    return response


def lambda_handler(event, context):
    bucket = 'chicolambdatest'
    key = 'rent3'
    csv=downloadCSV(key)

    try:
        response = s3.put_object(Bucket=bucket, Key=key, Body=csv)
        print('upload ok')
        print(csv)
        #return response

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
