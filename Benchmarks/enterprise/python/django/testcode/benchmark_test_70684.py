# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70684(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
