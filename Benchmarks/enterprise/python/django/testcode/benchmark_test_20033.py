# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest20033(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
