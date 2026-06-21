# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20904(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
