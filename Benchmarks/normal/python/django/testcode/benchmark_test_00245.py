# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import urllib.request
from app_runtime import db


def BenchmarkTest00245(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
