
import json

def handler(event, context):    
    body = json.loads(event['body'])
    print(body)
    return {
        'statusCode': 200,
        'body': json.dumps(body),
        'headers': {
            'Access-Control-Allow-Origin': True,
            'Access-Control-Allow-Origin': "' *'",
            'Content-Type': 'application/json'
        }
    }
