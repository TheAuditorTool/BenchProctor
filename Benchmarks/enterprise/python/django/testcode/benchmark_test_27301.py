# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27301(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
