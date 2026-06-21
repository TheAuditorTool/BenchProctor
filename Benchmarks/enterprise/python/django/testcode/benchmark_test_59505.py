# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast
from app_runtime import auth_check


def BenchmarkTest59505(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
