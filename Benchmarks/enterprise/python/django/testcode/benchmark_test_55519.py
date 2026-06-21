# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55519(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
