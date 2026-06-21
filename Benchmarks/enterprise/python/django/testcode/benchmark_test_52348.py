# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52348(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
