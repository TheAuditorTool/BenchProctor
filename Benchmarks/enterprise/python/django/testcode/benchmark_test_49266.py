# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49266(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
