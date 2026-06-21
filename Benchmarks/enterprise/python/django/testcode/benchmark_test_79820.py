# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json
import ast


def BenchmarkTest79820(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
