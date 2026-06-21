# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17081(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
