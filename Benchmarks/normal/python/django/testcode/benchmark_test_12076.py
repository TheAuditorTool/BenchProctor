# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest12076(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = ua_value
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
