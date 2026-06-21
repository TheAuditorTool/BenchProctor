# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76933(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
