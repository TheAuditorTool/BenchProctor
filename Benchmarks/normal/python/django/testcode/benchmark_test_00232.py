# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
import re


def BenchmarkTest00232(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
