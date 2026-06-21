# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41127(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
