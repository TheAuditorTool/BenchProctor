# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast


def BenchmarkTest60015(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
