# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79451(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
