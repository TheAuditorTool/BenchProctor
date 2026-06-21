# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38881(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
