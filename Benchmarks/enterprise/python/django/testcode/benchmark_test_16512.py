# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16512(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
