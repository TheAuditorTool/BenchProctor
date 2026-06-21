# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest05493(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(yaml_value), store_cred)
    return JsonResponse({"saved": True})
