# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23337(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
