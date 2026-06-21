# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08798(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
