# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77709(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
