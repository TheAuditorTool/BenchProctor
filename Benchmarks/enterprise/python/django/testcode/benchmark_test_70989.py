# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70989(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
