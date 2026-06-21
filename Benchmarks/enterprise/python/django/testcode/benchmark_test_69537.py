# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69537(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
