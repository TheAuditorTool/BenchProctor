# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37973(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(origin_value) + ',data\n')
    return JsonResponse({"saved": True})
