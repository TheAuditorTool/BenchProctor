# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24592(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    eval(str(data))
    return JsonResponse({"saved": True})
