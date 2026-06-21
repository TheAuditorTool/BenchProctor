# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54145(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
