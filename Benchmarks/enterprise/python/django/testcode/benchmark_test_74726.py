# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
from app_runtime import db


def BenchmarkTest74726(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
