# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74271(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
