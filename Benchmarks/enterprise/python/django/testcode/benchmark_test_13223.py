# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest13223(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
