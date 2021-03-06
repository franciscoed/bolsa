from __future__ import print_function

import json
import boto3
import csv

print('Loading function')

s3 = boto3.client('s3')
sns = boto3.client('sns')
dynamo = boto3.client('dynamodb')
#dynamodb.put_item(TableName=TSI, Item={'Name':{'S': str(key)},'key2':{'N':'value2'})
#dynamodb.get_item(TableName=TSI, Key={'Name':{'S':'Banana'}})


def closeList (csv):
    tempList = []
    subList = []
    for i in range(len(csv)):
        if i == 0:
            continue
        subList = str(csv[i]).split(',')
        tempList.append(subList[4])
    tempList.reverse()
    return tempList



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

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        csvReader = response['Body'].read().decode("utf-8")
        ListTotal = str(csvReader).splitlines()
        ListValues = closeList(ListTotal)



        return envio


    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
