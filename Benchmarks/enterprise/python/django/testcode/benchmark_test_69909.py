# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69909(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
