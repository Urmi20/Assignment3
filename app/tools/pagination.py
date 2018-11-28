import boto3
import pandas as pnd
from boto3.dynamodb.conditions import Attr


class Pagination:

    @staticmethod
    def scan_page(esk=None, limit=5,
                  project_input=None,
                  document_input=None,
                  discipline_input=None,
                  sentiment_input=None,
                  status_input=None):

        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        if esk is None:
            if (project_input is None and
                    document_input is None and
                    discipline_input is None and
                    sentiment_input is None and
                    status_input is None):
                scan_generator = table.scan()

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input))

        else:
            scan_generator = table.scan(params, Limit=limit, ExclusiveStartKey=esk)
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
