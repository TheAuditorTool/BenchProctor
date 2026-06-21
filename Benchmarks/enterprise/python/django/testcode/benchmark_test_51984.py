# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51984(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
