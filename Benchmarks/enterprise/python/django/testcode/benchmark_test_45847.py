# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest45847(request, path_param):
    path_value = path_param
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = path_value
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
