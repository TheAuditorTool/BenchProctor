# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18658(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
