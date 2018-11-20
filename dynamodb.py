import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'DynamoExample'
existing_tables = dynamodb.list_tables()['TableNames']


def create_new_table():
    table = dynamodb.create_table(
        TableName='DynamoExample',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 123,
            'WriteCapacityUnits': 123
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='DynamoExample')

    # Print out some data about the table.
    print(table.item_count)


if table_name not in existing_tables:
    #Table Creation
    create_new_table()

table = dynamodb.Table(table_name)

#Creating a new Item
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)

#Getting an Item
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)

#Update an Item
table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)

#Delete an Item
table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)




