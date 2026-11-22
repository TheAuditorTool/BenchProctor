# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00183(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
