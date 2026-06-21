# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71395(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
