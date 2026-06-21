# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61098(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
