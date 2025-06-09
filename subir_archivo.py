import boto3
import base64
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    bucket = body['bucket']
    key = body['key']
    contenido_base64 = body['contenido_base64']

    try:
        contenido = base64.b64decode(contenido_base64)
        s3.put_object(Bucket=bucket, Key=key, Body=contenido)
        return {'statusCode': 200, 'body': f'Se subió {key} en el bucket {bucket}'}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
