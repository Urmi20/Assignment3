import boto3
import pandas as pnd
import numpy as nmp
from boto3.dynamodb.conditions import Attr


class Pagination:

    @staticmethod
    def scan_page(esk=None,
                  project_input=None,
                  document_input=None,
                  discipline_input=None,
                  sentiment_input=None,
                  status_input=None,
                  limit=5):

        dynamodb = boto3.resource('dynamodb')
        table_name = 'it_issues'

        table = dynamodb.Table(table_name)

        if esk is None:
            if (project_input is None and
                    document_input is None and
                    discipline_input is None and
                    sentiment_input is None and
                    status_input is None):
                scan_generator = table.scan(Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), Limit=limit)


        else:
            if (project_input is None and
                    document_input is None and
                    discipline_input is None and
                    sentiment_input is None and
                    status_input is None):
                scan_generator = table.scan(ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input),
                                            ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)

            elif (project_input is not None and
                  document_input is not None and
                  discipline_input is not None and
                  sentiment_input is not None and
                  status_input is not None):
                scan_generator = table.scan(FilterExpression=Attr("project").eq(project_input) &
                                                             Attr("document").eq(document_input) &
                                                             Attr("discipline").eq(discipline_input) &
                                                             Attr("sentiment").eq(sentiment_input) &
                                                             Attr("status").eq(status_input), ExclusiveStartKey=esk, Limit=limit)
        last_evaluated_key = scan_generator.get('LastEvaluatedKey')
        issues_dict = scan_generator.get('Items')
        issue = pnd.DataFrame(issues_dict)
        issue_arr = issue.values
        return issue_arr, last_evaluated_key

    @staticmethod
    def data(esk=None,
                  project_input=None,
                  document_input=None,
                  discipline_input=None,
                  sentiment_input=None,
                  status_input=None,
                  final_arr=[],
                   limit=5):

        issues, last_evaluated_key = Pagination.scan_page(esk,
                                                          project_input,
                                                          document_input,
                                                          discipline_input,
                                                          sentiment_input,
                                                          status_input,
                                                          limit)
        if len(issues) > 0 and len(final_arr) > 0:
            issues = nmp.concatenate((issues, final_arr), axis=0)

        if len(issues) == 0 and len(final_arr) > 0:
            issues = final_arr

        return issues, last_evaluated_key

    @staticmethod
    def page_data(esk=None,
                  project_input=None,
                  document_input=None,
                  discipline_input=None,
                  sentiment_input=None,
                  status_input=None,
                  limit=5):

        last_evaluated_key = esk


        issues, last_evaluated_key = Pagination.scan_page(last_evaluated_key,
                                                              project_input,
                                                              document_input,
                                                              discipline_input,
                                                              sentiment_input,
                                                              status_input,
                                                              limit)

        while len(issues) < limit and last_evaluated_key is not None:
            issues, last_evaluated_key = Pagination.data(last_evaluated_key,
                                                          project_input,
                                                          document_input,
                                                          discipline_input,
                                                          sentiment_input,
                                                          status_input,
                                                          issues,
                                                          limit)

        return issues, last_evaluated_key

    @staticmethod
    def get_all_filtered_issues(
                  project_input=None,
                  document_input=None,
                  discipline_input=None,
                  sentiment_input=None,
                  status_input=None):

        issues = None
        last_key = None

        issues, last_key = Pagination.page_data(last_key, project_input, document_input, discipline_input,
                                                     sentiment_input, status_input, 5)

        while last_key:
            curr_issues, last_key = Pagination.page_data(last_key, project_input, document_input, discipline_input,
                                                        sentiment_input, status_input, 5)
            if len(curr_issues) > 0 and len(issues) > 0:
                issues = nmp.concatenate((issues, curr_issues), axis=0)

            if len(issues) == 0 and len(curr_issues) > 0:
                issues = curr_issues

        return issues
