# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest25404(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
