# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55259(request):
    cookie_value = request.COOKIES.get('session_token', '')
    globals().setdefault('_secret_cache', {})['current'] = str(cookie_value)
    return JsonResponse({"saved": True})
