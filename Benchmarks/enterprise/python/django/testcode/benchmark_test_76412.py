# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest76412(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
