# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import db


def BenchmarkTest55576(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
