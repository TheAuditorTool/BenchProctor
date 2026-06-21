# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00949(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    processed = data[:64]
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
