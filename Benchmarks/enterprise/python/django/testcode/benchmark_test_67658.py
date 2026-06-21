# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import ast


def BenchmarkTest67658(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
