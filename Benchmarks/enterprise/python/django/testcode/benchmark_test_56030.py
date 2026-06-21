# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest56030(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
