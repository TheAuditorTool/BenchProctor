# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38439(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
