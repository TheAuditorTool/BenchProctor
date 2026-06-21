# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63350(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
