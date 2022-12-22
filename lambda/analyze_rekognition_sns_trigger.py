import json
import logging
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    logging.basicConfig(format = '%(asctime)s : %(levelname)s %(message)s')
    log.info(event)
    snsType = event['Records'][0]['Sns']['Type']
    snsMessage = json.loads(event['Records'][0]['Sns']['Message'])
    log.info(snsMessage)
    snsJobId = snsMessage['JobId']
    snsJobStatus = snsMessage['Status']
    snsJobTag = snsMessage['JobTag']
    rekognition = boto3.client('rekognition')
    if snsJobStatus == 'SUCCEEDED':
        rekognition_response_labels = rekognition.get_label_detection(JobId=snsJobId)
        log.info(f"The label response is {rekognition_response_labels}")
        labels = rekognition_response_labels['Labels']
        for label_detail in labels:
            if label_detail['Label']['Name'] == 'Knife' or label_detail['Label']['Name'] == 'Gun' or label_detail['Label']['Name'] == 'Weapon':
                SENDER = "admin@milind.works"
                RECIPIENT = 'milind.basavaraja@nyu.edu'

                AWS_REGION = "us-east-1"

                # The email to send.
                SUBJECT = "Nyu Campus Safety Survelliance - Safety Mail"
                #BODY_TEXT = "Hello admin, A weapon is detected in the video. Beware!Beware!"
                BODY_TEXT = """<html>
                                            <head></head>
                                            <body>
                                                <h1>NYU Campus Safety Survelliance - Safety Mail</h1>
                                                <h3> Hi Admin,</h3>
                                                <p> Please be advised, an unauthorised weapon has been identified in the campus premises CCTV #1393. Take appropriate actions.</p>
                                                <h3>Regards,</p>
                                                <h5>NYU Campus SAFETY Survelliance</h5>
                                            </body>
                                            </html>"""  
                CHARSET = "UTF-8"
                client = boto3.client('ses',region_name=AWS_REGION)
    
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
                    break
                except ClientError as e:
                    print(e.response['Error']['Message'])
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
