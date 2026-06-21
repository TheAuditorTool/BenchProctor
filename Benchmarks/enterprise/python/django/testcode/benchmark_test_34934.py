# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import ast


def BenchmarkTest34934(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
