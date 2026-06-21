# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49757(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
