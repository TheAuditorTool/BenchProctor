# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01823(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return JsonResponse({"saved": True})
