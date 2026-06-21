# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28699(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
