# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38088(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
