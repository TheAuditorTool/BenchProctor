# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23571(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
