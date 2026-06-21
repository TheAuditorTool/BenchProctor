# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70392(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
