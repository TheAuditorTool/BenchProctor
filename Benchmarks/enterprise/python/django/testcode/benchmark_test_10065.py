# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest10065(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
