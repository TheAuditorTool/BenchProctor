# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import json
from app_runtime import auth_check


def BenchmarkTest21280(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json_value if json_value else 'default'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
