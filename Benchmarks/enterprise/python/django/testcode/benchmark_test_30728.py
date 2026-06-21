# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import requests


def BenchmarkTest30728(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
