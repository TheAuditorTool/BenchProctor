# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import ast
from app_runtime import db


def BenchmarkTest21767(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
