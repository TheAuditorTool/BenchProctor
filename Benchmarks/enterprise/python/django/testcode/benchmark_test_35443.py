# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest35443(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
