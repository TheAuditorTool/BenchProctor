# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08179(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
