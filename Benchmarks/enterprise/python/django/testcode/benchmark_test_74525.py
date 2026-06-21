# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest74525(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
