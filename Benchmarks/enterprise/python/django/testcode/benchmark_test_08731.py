# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3
from app_runtime import ssm_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08731(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    ctx = RequestContext(ssm_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
