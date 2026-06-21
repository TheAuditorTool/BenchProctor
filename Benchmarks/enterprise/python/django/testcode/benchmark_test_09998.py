# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09998(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
