# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65157(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
