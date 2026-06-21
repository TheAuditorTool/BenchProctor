# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import db


def BenchmarkTest53200(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
