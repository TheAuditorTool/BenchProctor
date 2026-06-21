# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70425(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
