# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest05636(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
