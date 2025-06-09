import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']

    try:
        s3.put_object(Bucket=bucket, Key=(directorio.strip('/') + '/'))
        return {'statusCode': 200, 'body': f'Directorio {directorio}/ creado en bucket {bucket}'}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
