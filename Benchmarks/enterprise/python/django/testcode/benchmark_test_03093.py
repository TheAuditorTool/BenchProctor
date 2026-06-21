# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03093(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
