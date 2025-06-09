import boto3, base64, json

def lambda_handler(event, context):
    body = event['body']
    if isinstance(body, str): body = json.loads(body)

    try:
        data = base64.b64decode(body['contenido_base64'])
        boto3.client('s3').put_object(Bucket=body['bucket'], Key=body['key'], Body=data)
        return {'statusCode': 200, 'body': f"Archivo '{body['key']}' subido"}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}
