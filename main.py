import json
import boto3

def lambda_handler(event, context):
     client = boto3.client("dynamodb")
     resp = client.scan(TableName="view_count", AttributesToGet=["total_count"])
     current_count = int(resp["Items"][0]["total_count"]["S"])
     current_count += 1
     client.put_item(
                TableName="view_count",
                Item={
                    "total_count": {"S": str(current_count)}
                }
            )
     
     return {
         'statusCode': 200,
         'body': json.dumps(current_count)
         
     }