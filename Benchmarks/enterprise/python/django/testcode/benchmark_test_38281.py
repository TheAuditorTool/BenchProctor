# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38281(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
