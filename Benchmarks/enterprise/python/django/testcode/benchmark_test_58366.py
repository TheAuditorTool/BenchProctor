# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58366(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if len(str(cookie_value)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
