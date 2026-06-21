# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest57380(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = to_text(prop_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
