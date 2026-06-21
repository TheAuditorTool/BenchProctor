# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18970(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
