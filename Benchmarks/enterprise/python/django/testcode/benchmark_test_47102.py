# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47102(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
