# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def ensure_str(value):
    return str(value)

def BenchmarkTest12123(request):
    xml_value = request.body.decode('utf-8')
    data = ensure_str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
