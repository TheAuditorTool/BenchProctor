# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56076(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
