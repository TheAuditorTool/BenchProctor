# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
import ast


def BenchmarkTest02255(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
