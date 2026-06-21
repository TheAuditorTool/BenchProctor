# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40941(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
