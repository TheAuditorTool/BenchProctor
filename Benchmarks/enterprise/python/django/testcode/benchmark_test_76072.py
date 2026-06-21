# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76072(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    os.remove(str(data))
    return JsonResponse({"saved": True})
