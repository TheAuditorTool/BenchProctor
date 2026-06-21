# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36412(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
