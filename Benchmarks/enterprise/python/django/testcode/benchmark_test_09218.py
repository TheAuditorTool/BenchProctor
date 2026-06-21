# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09218(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
