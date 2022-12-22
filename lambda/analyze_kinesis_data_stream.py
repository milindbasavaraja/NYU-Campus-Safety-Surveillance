import json
import base64
from datetime import datetime,timedelta
import boto3
from botocore.exceptions import ClientError

client = boto3.client('ses',region_name='us-east-1')


def lambda_handler(event, context):
    print(event)
    record = event['Records'][0]
    print(record)
    load = base64.b64decode(record['kinesis']['data']).decode('utf-8')
    payload = json.loads(load)
    print(payload)
    timestamp = payload['InputInformation']['KinesisVideo']['ProducerTimestamp']
    dt_object = datetime.fromtimestamp(timestamp) - timedelta(hours=5, minutes=0)
    face_search_response = payload['FaceSearchResponse']
    unrecognised_faces = 0
    for face_search in face_search_response:
        if len(face_search['MatchedFaces']) != 0:
            print(face_search['MatchedFaces'][0]['Face']['ExternalImageId'])
        else:
            print("Un-authorized face detected")
            unrecognised_faces = unrecognised_faces+1
            
            
            
    SENDER = "admin@milind.works"
    RECIPIENT = 'milind.basavaraja@nyu.edu'
    AWS_REGION = "us-east-1"

    # The email to send.
    SUBJECT = "Nyu Campus Safety Survelliance - Safety Mail"
    BODY_TEXT = """<html>
                   <head></head>
                   <body>
                       <h1>NYU Campus Safety Survelliance - Safety Mail</h1>
                       <h3> Hi Admin,</h3>
                       <p> Please be advised, an unauthorised person has been identified in the campus premises CCTV #1393. Take appropriate actions.</p>
                       <h3>Regards,</p>
                       <h3>NYU Campus SAFETY Survelliance</h5>
                    </body>
                    </html>"""  
    CHARSET = "UTF-8"
            
    
     # Try to send the email.
    try:
    #Provide the contents of the email.
        response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
            
        )
    except ClientError as e:
                print(e.response['Error']['Message'])
    print(dt_object)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
