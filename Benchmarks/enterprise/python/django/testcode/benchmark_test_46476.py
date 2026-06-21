# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast
import pickle


def BenchmarkTest46476(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
