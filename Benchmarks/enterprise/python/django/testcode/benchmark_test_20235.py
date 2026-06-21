# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20235(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        result = int(str(referer_value))
    except Exception:
        pass
    return JsonResponse({"saved": True})
