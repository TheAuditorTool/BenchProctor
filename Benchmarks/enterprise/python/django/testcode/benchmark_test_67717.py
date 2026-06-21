# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67717(request):
    cookie_value = request.COOKIES.get('session_token', '')
    size = min(int(cookie_value) if str(cookie_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
