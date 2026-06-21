# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03247(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
