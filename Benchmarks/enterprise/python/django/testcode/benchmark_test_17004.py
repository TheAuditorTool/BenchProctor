# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17004(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
