# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
from app_runtime import db


def BenchmarkTest14596(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
