# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08418(request):
    secret_value = 'default_setting_value'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
