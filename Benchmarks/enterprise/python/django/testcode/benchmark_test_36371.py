# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36371(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
