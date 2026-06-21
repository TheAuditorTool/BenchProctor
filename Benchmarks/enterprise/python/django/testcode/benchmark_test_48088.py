# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48088(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
