# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04048(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
