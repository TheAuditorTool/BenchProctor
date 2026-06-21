# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest33273(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
