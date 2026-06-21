# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72937(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(referer_value))
    return JsonResponse({"saved": True})
