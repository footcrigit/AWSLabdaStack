import logging
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('staff')
    response = table.query(
    KeyConditionExpression=Key('MovieID').eq('1') & Key('ReleaseYear').eq('2019')
    )
    return {
        'statuscode' : 200,
        'body' : json.dumps(response)
    }