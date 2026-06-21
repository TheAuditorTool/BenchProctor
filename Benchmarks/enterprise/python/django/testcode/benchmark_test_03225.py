# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03225(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
