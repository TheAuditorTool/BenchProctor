# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


request_state: dict[str, str] = {}

def BenchmarkTest15558(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    request_state['last_input'] = yaml_value
    data = request_state['last_input']
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
