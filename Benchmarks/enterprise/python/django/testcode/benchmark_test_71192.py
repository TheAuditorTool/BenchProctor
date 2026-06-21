# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71192(request):
    xml_value = request.body.decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
