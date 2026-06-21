# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37464(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
