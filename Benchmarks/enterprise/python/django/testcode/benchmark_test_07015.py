# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07015(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
