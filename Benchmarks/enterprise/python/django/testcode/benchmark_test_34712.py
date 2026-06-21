# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
import ast
from app_runtime import auth_check


def BenchmarkTest34712(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
