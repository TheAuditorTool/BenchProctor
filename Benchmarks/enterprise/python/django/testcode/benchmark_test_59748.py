# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59748(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
