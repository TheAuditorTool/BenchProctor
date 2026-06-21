# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest04914(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = header_value
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
