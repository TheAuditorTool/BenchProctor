# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36137(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
