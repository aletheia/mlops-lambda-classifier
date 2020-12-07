
import json

from classifier import ChurnClassifier

def handler(event, context):    
    #body = json.loads(event['body'])
    body = json.loads(event['body'])
    print(body)
    classifier = ChurnClassifier()
    res = classifier.predict(body)
    print('Got data')
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps({"churn status":res}),
        'headers': {
            'Access-Control-Allow-Origin': True,
            'Access-Control-Allow-Origin': "' *'",
            'Content-Type': 'application/json'
        }
    }
