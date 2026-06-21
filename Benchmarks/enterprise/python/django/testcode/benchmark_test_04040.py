# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import ast
from app_runtime import auth_check


def BenchmarkTest04040(request):
    secret_value = 'default_setting_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
