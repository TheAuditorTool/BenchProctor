# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56760(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
