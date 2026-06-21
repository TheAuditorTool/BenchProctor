# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest46637(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
