# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast
from app_runtime import db


def BenchmarkTest01132(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
