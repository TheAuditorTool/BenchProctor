# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest32369(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    eval(str(data))
    return JsonResponse({"saved": True})
