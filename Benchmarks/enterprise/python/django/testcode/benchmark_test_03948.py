# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import yaml
from app_runtime import ssm_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03948(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    ctx = RequestContext(ssm_value)
    data = ctx.payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
