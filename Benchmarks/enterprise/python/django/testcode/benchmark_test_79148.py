# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79148(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
