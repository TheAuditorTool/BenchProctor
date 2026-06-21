# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31194(request):
    host_value = request.META.get('HTTP_HOST', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(host_value))
    return JsonResponse({"saved": True})
