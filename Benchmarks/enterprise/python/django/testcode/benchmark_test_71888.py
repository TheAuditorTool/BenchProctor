# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import urllib.request


def BenchmarkTest71888(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
