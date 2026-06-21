# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68766(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
