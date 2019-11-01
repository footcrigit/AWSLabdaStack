import logging
import json

def lambda_handler(event,context):
    resp = {
        "message" : "lambda tested successfully"
    }
    return {
        'statuscode' : 200,
        'body' : json.dumps(resp)
    }