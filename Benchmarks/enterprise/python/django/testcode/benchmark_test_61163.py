# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61163(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        result = int(str(ua_value))
    except Exception:
        pass
    return JsonResponse({"saved": True})
