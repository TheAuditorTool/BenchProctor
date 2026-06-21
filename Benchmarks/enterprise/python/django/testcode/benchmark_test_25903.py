# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25903(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
