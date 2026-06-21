# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest06397(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
