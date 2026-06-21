# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest09636(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
