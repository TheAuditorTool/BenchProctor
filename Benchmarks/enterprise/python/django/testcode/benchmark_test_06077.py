# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06077(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
