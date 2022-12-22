import json
import boto3
from botocore.exceptions import ClientError

rekognition = boto3.client('rekognition')

def describe_collection():
    
    try:
        print("Describing the collection details")
        response = rekognition.describe_collection(CollectionId='nyu-student-collection-2022')
        print(response)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print ('The collection ' + collection_id + ' was not found ')
        else:
            print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
            

def add_face_to_collection(bucket_name,image_name):
    
    print(f"Adding face {image_name} to collection")
    response = rekognition.index_faces(
            CollectionId='nyu-student-collection-2022',
            Image={'S3Object':{'Bucket':bucket_name,'Name':image_name}},
            ExternalImageId='Milind',
            QualityFilter="AUTO",
            DetectionAttributes=['ALL']
            
        )
        
    print(f"Response after adding face {response}")

def list_faces_in_collection():
    response = rekognition.list_faces(CollectionId='nyu-student-collection-2022')
    print(f"Face List is {response}")

def lambda_handler(event, context):
    print(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    describe_collection()
    #add_face_to_collection(bucket_name,image_name)
    list_faces_in_collection()
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
