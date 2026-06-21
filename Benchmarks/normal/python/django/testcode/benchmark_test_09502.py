# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09502(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ctx = RequestContext(yaml_value)
    data = ctx.payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
