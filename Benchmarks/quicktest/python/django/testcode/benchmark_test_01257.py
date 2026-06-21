# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest01257(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
