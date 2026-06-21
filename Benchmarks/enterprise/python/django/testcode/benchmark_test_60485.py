# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import auth_check


def BenchmarkTest60485(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
