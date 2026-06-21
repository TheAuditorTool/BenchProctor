# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
import ast


def BenchmarkTest41843(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
