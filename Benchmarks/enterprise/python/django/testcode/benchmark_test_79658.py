# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79658(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
