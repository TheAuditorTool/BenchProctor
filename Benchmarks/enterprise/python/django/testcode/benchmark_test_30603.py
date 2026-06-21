# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30603(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
