# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
from app_runtime import db


def BenchmarkTest63696(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
