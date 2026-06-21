# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import ast
from app_runtime import auth_check


def BenchmarkTest59933(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = str(ast.literal_eval(file_value))
    except (ValueError, SyntaxError):
        data = file_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
