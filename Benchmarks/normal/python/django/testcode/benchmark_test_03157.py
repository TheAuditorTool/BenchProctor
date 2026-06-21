# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03157(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
