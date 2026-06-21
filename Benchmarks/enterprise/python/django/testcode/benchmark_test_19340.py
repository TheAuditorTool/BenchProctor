# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast


def BenchmarkTest19340(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
