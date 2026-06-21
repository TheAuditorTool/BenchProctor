# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest48198(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
