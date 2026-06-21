# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73544(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    int(str(data))
    return JsonResponse({"saved": True})
