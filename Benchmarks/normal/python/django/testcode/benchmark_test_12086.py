# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12086(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
