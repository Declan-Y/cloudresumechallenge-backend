import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    current_count = get_current_count(client)

    current_count = increment_count(current_count)
    
    update_count(current_count)
    return {
          'headers': {
            'Access-Control-Allow-Origin': '*'
        },
         'statusCode': 200,
         'body': json.dumps(current_count)
         
     }

def get_current_count(client):
     resp = client.scan(TableName="view_count", AttributesToGet=["total_count"])
     current_count = int(resp["Items"][0]["total_count"]["S"])

     return current_count


def increment_count(current_count):
     new_count = current_count + 1
     return new_count


def update_count(client, current_count):
     client.put_item(
                TableName="view_count",
                Item={
                    "total_count": {"S": str(current_count)}
                }
            )
