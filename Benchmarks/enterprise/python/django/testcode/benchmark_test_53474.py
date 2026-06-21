# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53474(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
