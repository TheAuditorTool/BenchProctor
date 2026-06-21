# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45434(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
