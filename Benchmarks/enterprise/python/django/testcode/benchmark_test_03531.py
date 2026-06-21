# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03531(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    eval(str(data))
    return JsonResponse({"saved": True})
