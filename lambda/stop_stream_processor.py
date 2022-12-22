import json
import boto3

def lambda_handler(event, context):
    rekognition = boto3.client('rekognition')
    response = rekognition.stop_stream_processor(
    Name='demo-stream-processor-1'
)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps('Stopped Stream Processor')
    }
