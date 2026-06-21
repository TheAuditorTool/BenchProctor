# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest21649(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = origin_value
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
