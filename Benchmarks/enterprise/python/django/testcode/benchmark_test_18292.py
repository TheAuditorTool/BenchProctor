# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18292(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
