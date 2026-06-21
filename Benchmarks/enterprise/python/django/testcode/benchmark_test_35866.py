# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35866(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
