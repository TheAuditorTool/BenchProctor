# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import ast
from app_runtime import auth_check


def BenchmarkTest21027(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = str(ast.literal_eval(config_value))
    except (ValueError, SyntaxError):
        data = config_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
