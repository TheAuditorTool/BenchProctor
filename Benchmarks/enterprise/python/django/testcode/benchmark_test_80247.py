# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80247(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    int(str(data))
    return JsonResponse({"saved": True})
