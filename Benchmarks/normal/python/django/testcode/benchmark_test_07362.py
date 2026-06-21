# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07362(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
