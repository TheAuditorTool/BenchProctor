# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest31849(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(prop_value), store_cred)
    return JsonResponse({"saved": True})
