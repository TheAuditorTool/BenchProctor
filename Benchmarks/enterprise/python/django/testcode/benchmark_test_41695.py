# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41695(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    exec(str(data))
    return JsonResponse({"saved": True})
