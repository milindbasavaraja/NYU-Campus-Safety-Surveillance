import json
import boto3

def create_collection(collection_id):
    client = boto3.client('rekognition')
    
    response = client.create_collection(CollectionId = collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    

def lambda_handler(event, context):
    create_collection("nyu-student-collection-2022")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
