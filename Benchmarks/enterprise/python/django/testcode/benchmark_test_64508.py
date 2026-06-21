# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64508(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if str(referer_value) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
