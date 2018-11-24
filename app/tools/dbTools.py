import boto3
from boto3.dynamodb.conditions import Key
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from os import urandom
from base64 import b64encode

key = urandom(24)
secret_key = b64encode(key).decode('utf-8')


class DataBaseManager:
    @staticmethod
    def add_user(username, first_name, last_name, email, password):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        table.put_item(
            Item={
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
            }
        )

        return True

    @staticmethod
    def email_already_exists(email):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        response = table.scan(
            FilterExpression=Key('email').eq(email),
        )

        while 'LastEvaluatedKey' in response:
            response = table.scan(
                FilterExpression=Key('email').eq(email),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )

        item = response['Items']

        if not item:
            return False

        return True

    @staticmethod
    def get_user_pwd_hash(username):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        response = table.get_item(
            Key={
                'username': username,
            }
        )

        item = response['Item']

        if item:
            salt, pw_hash = DataBaseManager.split_salt_hash(item.get('password'))

        return salt, pw_hash

    @staticmethod
    def split_salt_hash(salt_hash):
        salt, pw_hash = salt_hash.rsplit("$", 1)
        salt = salt[1:]
        return salt, pw_hash

    def update_new_password(self, new_pwd, email):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        response = table.scan(
            FilterExpression=Key('email').eq(email),
        )

        while 'LastEvaluatedKey' in response:
            response = table.scan(
                FilterExpression=Key('email').eq(email),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )

        item = response['Items']

        if item:
            username = item[0].get('username')

            table.update_item(
                Key={
                    'username': username,
                },
                UpdateExpression='SET password = :new_pwd',
                ExpressionAttributeValues={
                    ':new_pwd': new_pwd
                }
            )
        else:
            return False

        return True

    @staticmethod
    def get_token(email, expires_sec=300):
        s = Serializer(secret_key, expires_sec)
        return s.dumps({'user_id': email}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        s = Serializer(secret_key)
        try:
            user_email = s.loads(token)['user_id']
        except:
            return None
        return user_email
