# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54247(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
