import boto3
import pymysql
import os

# AWS clients
rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

# RDS connection settings
rds_host = "database-1.crgkus0w2ei8.ap-south-1.rds.amazonaws.com"   # from RDS console
db_username = "admin"
db_password = "Iantpln1232025"
db_name = "PhotoApp"

def lambda_handler(event, context):
    # Get bucket and image key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    image_key = event['Records'][0]['s3']['object']['key']
    
    # Call Rekognition
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image_key}},
        MaxLabels=5
    )
    
    # Connect to RDS MySQL
    conn = pymysql.connect(
        host=rds_host,
        user=db_username,
        passwd=db_password,
        db=db_name,
        connect_timeout=10
    )
    
    try:
        with conn.cursor() as cursor:
            for label in response['Labels']:
                sql = """INSERT INTO PhotoLabels (ImageKey, Label, Confidence) 
                         VALUES (%s, %s, %s)"""
                cursor.execute(sql, (image_key, label['Name'], label['Confidence']))
        conn.commit()
    finally:
        conn.close()
    
    return {"status": "success", "image": image_key, "labels": response['Labels']}
