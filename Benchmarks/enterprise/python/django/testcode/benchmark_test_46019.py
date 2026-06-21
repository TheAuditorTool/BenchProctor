# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46019(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
