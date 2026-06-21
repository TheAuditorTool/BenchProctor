# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast
from app_runtime import db


def BenchmarkTest29918(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
