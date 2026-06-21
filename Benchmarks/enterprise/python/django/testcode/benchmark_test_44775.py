# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44775(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
