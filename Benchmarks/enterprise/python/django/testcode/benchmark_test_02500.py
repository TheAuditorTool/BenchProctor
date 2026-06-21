# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02500(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
