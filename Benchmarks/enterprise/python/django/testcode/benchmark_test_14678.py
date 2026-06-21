# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14678(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
