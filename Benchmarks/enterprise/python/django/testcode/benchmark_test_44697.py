# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest44697(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
