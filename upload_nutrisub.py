import boto3
import json

# Initialize DynamoDB Resource
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")  # Change region if needed
table_name = "NutriSubAI"  # Correct table name
table = dynamodb.Table(table_name)

# Load the corrected JSON data
with open("nutrisub_ai_dynamodb_new_table.json", "r") as file:
    data = json.load(file)

# Function to format data correctly for DynamoDB
def format_for_dynamodb(item):
    formatted_item = {}

    for key, value in item.items():
        if key == "ingredient":  # Ensure primary key is properly formatted
            formatted_item[key] = {"S": str(value["S"])}
        elif key == "substitutions":  # Ensure substitutions are stored as a list
            formatted_item[key] = {"L": [{"S": sub["S"]} for sub in value["L"]]}
        else:
            formatted_item[key] = {"S": str(value["S"])} if isinstance(value, dict) and "S" in value else {"S": str(value)}
    
    return formatted_item

# Batch Write (DynamoDB has a 25-item limit per batch)
def batch_write(items):
    with table.batch_writer() as batch:
        for item in items:
            formatted_item = format_for_dynamodb(item)
            batch.put_item(Item=formatted_item)
    print(f"Uploaded {len(items)} items successfully!")

# Split into batches of 25 (DynamoDB batch write limit)
batch_size = 25
for i in range(0, len(data), batch_size):
    batch_write(data[i:i+batch_size])

print("All data uploaded successfully!")
