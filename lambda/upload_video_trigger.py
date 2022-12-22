import json
import logging
import boto3
import random

def lambda_handler(event, context):
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    logging.basicConfig(format = '%(asctime)s : %(levelname)s %(message)s')
    client_request_token = random.randint(1000,10000)
    log.info(event)
    
    bucket_name = event['Records'][0]['s3']['bucket']['name'] 
    video_key = event['Records'][0]['s3']['object']['key']
    
    log.info(f"The bucket name is {bucket_name} and key is {video_key}")
    
    try:
       # s3 = boto3.client("s3")
       # response = s3.head_object(Bucket=bucket_name,Key=video_key)
       # log.info(f"The response is: {response}")
        log.info("Detecting video using rekognition")
        rekognition = boto3.client('rekognition')
        rekognition_response = rekognition.start_label_detection(
               Video={
                  'S3Object': {
                      'Bucket': bucket_name,
                     'Name': video_key
                    }
                },
                ClientRequestToken=f"test-video-{client_request_token}",
                NotificationChannel={
                    'SNSTopicArn': 'arn:aws:sns:us-east-1:104658801431:TestTopicAmazonRekognition',
                    'RoleArn': 'arn:aws:iam::104658801431:role/RekognitionRole'
                },
                JobTag='test-video-2'
            )
            
        log.info(f"The response is: {rekognition_response}")
            
    except Exception as exception:
        log.error(f"The error is: {exception}")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
