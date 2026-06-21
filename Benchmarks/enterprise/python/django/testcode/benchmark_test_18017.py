# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest18017(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
