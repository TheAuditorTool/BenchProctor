# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import time
import ast


def BenchmarkTest69672(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
