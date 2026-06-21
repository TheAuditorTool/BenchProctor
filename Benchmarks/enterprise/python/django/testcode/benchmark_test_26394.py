# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest26394(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
