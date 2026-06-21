# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09451(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
