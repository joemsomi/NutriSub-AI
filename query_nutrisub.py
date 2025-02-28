import boto3

# Initialize DynamoDB Resource
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("NutriSubAI")

# Query for a specific ingredient
response = table.get_item(Key={"ingredient": "sugar"})

# Print result
print(response.get("Item", "No item found"))