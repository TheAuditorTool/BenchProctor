# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13292(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(forwarded_ip) + ',data\n')
    return JsonResponse({"saved": True})
