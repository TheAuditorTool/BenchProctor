# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest76108(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
