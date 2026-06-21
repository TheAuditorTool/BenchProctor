# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import ast


def BenchmarkTest31442(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = data[:64]
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
