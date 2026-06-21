# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24915(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
