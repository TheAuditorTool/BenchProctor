# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02219(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
