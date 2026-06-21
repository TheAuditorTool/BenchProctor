# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53338(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
