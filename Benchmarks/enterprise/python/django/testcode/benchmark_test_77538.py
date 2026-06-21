# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77538(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
