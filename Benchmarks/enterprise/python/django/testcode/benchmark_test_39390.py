# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import ast


def BenchmarkTest39390(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
