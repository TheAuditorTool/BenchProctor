# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07547(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
