# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04099(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
