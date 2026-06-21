# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def BenchmarkTest25374(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
