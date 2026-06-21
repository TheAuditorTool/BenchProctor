# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59802(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
