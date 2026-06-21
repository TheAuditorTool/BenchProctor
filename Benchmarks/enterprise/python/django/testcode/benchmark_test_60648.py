# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import ast


def BenchmarkTest60648(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
