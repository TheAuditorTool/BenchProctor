# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os
import ast


def BenchmarkTest22955(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
