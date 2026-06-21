# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49086(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
