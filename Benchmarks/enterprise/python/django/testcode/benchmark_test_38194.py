# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38194(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    eval(str(data))
    return JsonResponse({"saved": True})
