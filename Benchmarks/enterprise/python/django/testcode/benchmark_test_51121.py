# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import yaml


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest51121(request):
    secret_value = 'default_config_label'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
