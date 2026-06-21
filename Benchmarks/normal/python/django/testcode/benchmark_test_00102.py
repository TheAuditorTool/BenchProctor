# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00102(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
