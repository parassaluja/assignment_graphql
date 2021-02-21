import json
import boto3

def lambda_handler(event, context):
    print(" **** one")
    db_conn = boto3.resource('dynamodb', region_name="ap-south-1").Table('order_payments')
    print(db_conn)
    print("**** two")
    response = db_conn.get_item(
    Key={
        'paymentid': 1
    })
    print(response['Item'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
