# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest40784(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
