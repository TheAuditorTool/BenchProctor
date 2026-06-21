# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48979(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
