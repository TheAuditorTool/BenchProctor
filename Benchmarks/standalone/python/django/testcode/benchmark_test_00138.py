# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00138(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    exec(str(data))
    return JsonResponse({"saved": True})
