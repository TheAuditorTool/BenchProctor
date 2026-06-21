# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import ast
from app_runtime import db


def BenchmarkTest01809(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
