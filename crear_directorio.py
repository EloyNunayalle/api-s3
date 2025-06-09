import boto3, json

def lambda_handler(event, context):
    body = event['body']
    if isinstance(body, str): body = json.loads(body)

    try:
        boto3.client('s3').put_object(Bucket=body['bucket'], Key=body['directorio'].strip('/') + '/')
        return {'statusCode': 200, 'body': f"Directorio '{body['directorio']}/' creado"}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
