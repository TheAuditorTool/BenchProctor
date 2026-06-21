# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57431(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
