# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest74667(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
