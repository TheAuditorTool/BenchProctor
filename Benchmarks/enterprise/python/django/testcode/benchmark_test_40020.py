# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest40020(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
