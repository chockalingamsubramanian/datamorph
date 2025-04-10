import boto3
import json

def write_to_dynamo(table_name, item):
    try:
        if isinstance(item, str):
            item = json.loads(item)  # Parse if passed as stringified JSON

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        response = table.put_item(Item=item)

        print(f"📤 Successfully wrote item to DynamoDB table '{table_name}'")
        return {"status": "success", "response": response}

    except Exception as e:
        print(f"[❌] Failed to write to DynamoDB: {e}")
        return {"error": str(e)}
