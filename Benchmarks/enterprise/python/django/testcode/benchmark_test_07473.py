# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest07473(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = str(ast.literal_eval(config_value))
    except (ValueError, SyntaxError):
        data = config_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
