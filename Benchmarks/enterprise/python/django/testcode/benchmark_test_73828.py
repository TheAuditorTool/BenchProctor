# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast


def BenchmarkTest73828(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
