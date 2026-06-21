# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest37899(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
