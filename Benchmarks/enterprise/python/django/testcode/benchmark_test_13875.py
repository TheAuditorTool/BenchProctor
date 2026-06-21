# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13875(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
