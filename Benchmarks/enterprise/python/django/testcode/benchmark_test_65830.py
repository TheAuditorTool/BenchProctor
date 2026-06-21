# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65830(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
