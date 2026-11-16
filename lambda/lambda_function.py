
import json
import boto3
import os
import urllib.parse
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')

OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
            source_key = urllib.parse.unquote_plus(
                record['s3']['object']['key']
            )

            response = s3.get_object(
                Bucket=source_bucket,
                Key=source_key
            )

            image_data = response['Body'].read()
            image = Image.open(BytesIO(image_data))
            image.thumbnail((800, 800), Image.Resampling.LANCZOS)

            output_buffer = BytesIO()
            image_format = image.format or 'JPEG'
            image.save(output_buffer, format=image_format)
            output_buffer.seek(0)

            output_key = 'resized/' + source_key

            s3.put_object(
                Bucket=OUTPUT_BUCKET,
                Key=output_key,
                Body=output_buffer,
                ContentType=response.get(
                    'ContentType', 'image/jpeg'
                )
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Image resized successfully!')
        }

    except Exception as e:
        print('Error:', str(e))
        raise
