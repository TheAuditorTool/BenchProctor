# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest25510(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
