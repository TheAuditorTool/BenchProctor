# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import re
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest35919(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
