# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest56980(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if str(processed) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
