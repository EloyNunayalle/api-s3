import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    nombre = body['nombre']

    try:
        s3.create_bucket(Bucket=nombre)
        return {'statusCode': 200, 'body': f'Se creó el bucket: {nombre}'}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
