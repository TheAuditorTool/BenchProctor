# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60026(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
