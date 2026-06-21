# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest30758(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
