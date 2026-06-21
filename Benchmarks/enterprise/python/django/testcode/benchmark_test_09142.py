# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
from app_runtime import db


def BenchmarkTest09142(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
