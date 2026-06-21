# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import boto3


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06432(request):
    secret_value = 'default_setting_value'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
