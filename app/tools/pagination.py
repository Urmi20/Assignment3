import boto3
import pandas as pnd


class Pagination:

    @staticmethod
    def scan_page(esk=None, limit=5):

        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        while True:
            if esk is None:
                scan_generator = table.scan(Limit=limit)
            else:
                scan_generator = table.scan(Limit=limit, ExclusiveStartKey=esk)
            last_evaluated_key = scan_generator.get('LastEvaluatedKey')
            issues_dict = scan_generator.get('Items')
            issue = pnd.DataFrame(issues_dict)
            issue_arr = issue.values
            return issue_arr, last_evaluated_key

    @staticmethod
    def page_data():
        issues, last_evaluated_key = Pagination.scan_page()
        while last_evaluated_key is not None:
            issues, last_evaluated_key = Pagination.scan_page(last_evaluated_key)
        return issues

