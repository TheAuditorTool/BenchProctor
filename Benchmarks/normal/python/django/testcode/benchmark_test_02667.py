# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import ast


def BenchmarkTest02667(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    os.seteuid(65534)
    return JsonResponse({"saved": True})
