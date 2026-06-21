# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast
from app_runtime import auth_check


def BenchmarkTest62209(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
