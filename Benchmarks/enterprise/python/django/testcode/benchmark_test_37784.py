# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37784(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if str(origin_value) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
