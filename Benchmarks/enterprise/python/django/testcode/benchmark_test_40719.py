# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import ast


def BenchmarkTest40719(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
