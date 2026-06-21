# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70400(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
