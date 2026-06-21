# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest38413(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
