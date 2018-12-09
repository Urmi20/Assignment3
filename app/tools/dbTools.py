import boto3
from boto3.dynamodb.conditions import Key
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from os import urandom
from base64 import b64encode

key = urandom(24)
secret_key = b64encode(key).decode('utf-8')


class DataBaseManager:
    @staticmethod
    def scan_filtered_table(table, key_name, key_value):
        response = table.scan(
            FilterExpression=Key(key_name).eq(key_value),
        )

        try:
            items = response['Items']
        except Exception as exception:
            items = dict()

        while 'LastEvaluatedKey' in response:
            response = table.scan(
                FilterExpression=Key(key_name).eq(key_value),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            try:
                items.extend(response['Items'])
            except Exception as excetion:
                continue

        return items

    @staticmethod
    def scan_table(table):
        response = table.scan()

        try:
            items = response['Items']
        except Exception as exception:
            items = dict()

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            try:
                items.extend(response['Items'])
            except Exception as excetion:
                continue

        return items


    @staticmethod
    def add_user(username, first_name, last_name, email, password):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        if DataBaseManager.check_existing_user_name(username):
            return False

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
    def check_existing_user_name(username):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        result = DataBaseManager.scan_filtered_table(table, 'username', username)
        if result:
            return True
        else:
            return False

    @staticmethod
    def email_already_exists(email):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_users'

        table = dynamodb.Table(table_name)

        items = DataBaseManager.scan_filtered_table(table, 'email', email)

        if not items:
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

        try:
            item = response['Item']
        except Exception as exception:
            item = list()

        salt = pw_hash = ''
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

        response = DataBaseManager.scan_filtered_table(table, 'email', email)

        if response:
            username = response[0].get('username')

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

    @staticmethod
    def get_projects():
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_projects'

        table = dynamodb.Table(table_name)

        items = DataBaseManager.scan_table(table)

        projects = list()
        for item in items:
            projects.append(item.get('name'))

        return projects

    @staticmethod
    def add_project(project_name):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_projects'

        table = dynamodb.Table(table_name)

        table.put_item(
            Item={
                'name': project_name,
            }
        )

        return True

    @staticmethod
    def get_documents_for(selected_project):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_documents'

        table = dynamodb.Table(table_name)

        items = DataBaseManager.scan_filtered_table(table, 'project', selected_project)

        documents = list()
        for item in items:
            documents.append(item.get('code'))

        return documents

    @staticmethod
    def add_document(project, document):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_documents'

        table = dynamodb.Table(table_name)

        table.put_item(
            Item={
                'code': document,
                'project': project
            }
        )

        return True

    @staticmethod
    def get_disciplines():
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_disciplines'

        table = dynamodb.Table(table_name)

        items = DataBaseManager.scan_table(table)

        disciplines = list()
        for item in items:
            disciplines.append(item.get('name'))

        return disciplines

    @staticmethod
    def add_issue(project, document, discipline,issue, date_time, id, sentiment, voice):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        try:
            table.put_item(
                Item={
                    'id': id,
                    'project': project,
                    'document': document,
                    'status': "Open",
                    'date_added': date_time,
                    'discipline': discipline,
                    'description': issue,
                    'sentiment': sentiment,
                    'voice': voice
                },
                ConditionExpression='attribute_not_exists(id)'
            )

        except Exception as exception:
            return False

        return True

    @staticmethod
    def get_issues():
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        items = DataBaseManager.scan_table(table)

        issues = list()
        for item in items:
            issues.append(item)

        return issues

    @staticmethod
    def update_issue_status(id, new_status):
        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        table.update_item(
            Key={
                'id': id,
            },
            UpdateExpression='SET #status = :new_status',
            ExpressionAttributeValues={
                ':new_status': new_status
            },
            ExpressionAttributeNames={
                "#status": "status"
            }
        )
