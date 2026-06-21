# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15925(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
