# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06655(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
