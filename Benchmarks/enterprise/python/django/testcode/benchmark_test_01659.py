# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import db


def BenchmarkTest01659(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
