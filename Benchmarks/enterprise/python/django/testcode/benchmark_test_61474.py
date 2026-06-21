# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
import ast


def BenchmarkTest61474(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
