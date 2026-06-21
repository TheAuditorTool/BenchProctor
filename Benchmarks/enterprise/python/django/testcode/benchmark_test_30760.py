# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30760(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
