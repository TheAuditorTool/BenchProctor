# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74252(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
