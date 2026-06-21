# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73821(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
