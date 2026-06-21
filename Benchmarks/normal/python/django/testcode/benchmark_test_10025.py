# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10025(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
