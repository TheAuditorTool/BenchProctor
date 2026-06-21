# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41983(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
