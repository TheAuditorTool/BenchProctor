# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast


def BenchmarkTest02932(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
