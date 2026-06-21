# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47143(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
