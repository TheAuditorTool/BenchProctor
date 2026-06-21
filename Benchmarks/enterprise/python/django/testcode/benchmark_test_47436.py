# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47436(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(origin_value))
    return JsonResponse({"saved": True})
