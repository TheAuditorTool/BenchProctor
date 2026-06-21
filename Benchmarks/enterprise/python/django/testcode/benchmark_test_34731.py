# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34731(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
