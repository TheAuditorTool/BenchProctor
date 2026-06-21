# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest77713(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
