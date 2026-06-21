# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45402(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
