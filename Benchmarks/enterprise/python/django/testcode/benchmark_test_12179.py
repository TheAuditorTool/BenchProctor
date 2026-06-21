# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest12179(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
