# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32177(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
