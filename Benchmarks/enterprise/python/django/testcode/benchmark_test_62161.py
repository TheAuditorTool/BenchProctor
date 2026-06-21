# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62161(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
