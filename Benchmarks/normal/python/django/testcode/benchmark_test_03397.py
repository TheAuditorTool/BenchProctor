# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast
from app_runtime import db


def BenchmarkTest03397(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
