# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06848(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
