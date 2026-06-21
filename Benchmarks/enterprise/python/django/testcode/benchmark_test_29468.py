# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29468(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
