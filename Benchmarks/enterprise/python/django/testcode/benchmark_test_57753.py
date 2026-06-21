# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57753(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
