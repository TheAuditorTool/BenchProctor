# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import json
from app_runtime import auth_check


def BenchmarkTest04885(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    try:
        data = json.loads(yaml_value).get('value', yaml_value)
    except (json.JSONDecodeError, AttributeError):
        data = yaml_value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
