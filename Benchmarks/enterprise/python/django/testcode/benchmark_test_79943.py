# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest79943(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    auth_check('user', data)
    return JsonResponse({"saved": True})
