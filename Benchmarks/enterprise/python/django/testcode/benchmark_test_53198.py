# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53198(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
