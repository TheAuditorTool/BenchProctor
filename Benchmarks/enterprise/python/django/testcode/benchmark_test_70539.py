# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70539(request):
    cookie_value = request.COOKIES.get('session_token', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(cookie_value))
    return JsonResponse({"saved": True})
