# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67012(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
