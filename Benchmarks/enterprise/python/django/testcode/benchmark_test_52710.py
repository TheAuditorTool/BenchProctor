# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast
from app_runtime import db


def BenchmarkTest52710(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
