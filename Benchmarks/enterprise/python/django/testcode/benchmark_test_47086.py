# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest47086(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
