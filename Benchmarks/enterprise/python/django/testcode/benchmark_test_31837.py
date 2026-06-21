# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31837(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
