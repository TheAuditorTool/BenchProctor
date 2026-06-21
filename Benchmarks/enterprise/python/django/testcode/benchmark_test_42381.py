# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42381(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
