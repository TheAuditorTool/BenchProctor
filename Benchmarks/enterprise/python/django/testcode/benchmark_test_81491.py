# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest81491(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
