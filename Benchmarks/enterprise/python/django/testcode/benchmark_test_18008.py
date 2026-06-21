# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest18008(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if auth_check('user', str(cookie_value)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
