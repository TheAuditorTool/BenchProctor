# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast
from app_runtime import db


def BenchmarkTest45017(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
