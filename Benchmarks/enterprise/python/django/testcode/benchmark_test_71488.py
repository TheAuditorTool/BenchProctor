# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71488(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
