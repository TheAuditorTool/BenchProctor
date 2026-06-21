# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import urllib.request
import urllib.parse
import ssl


def to_text(value):
    return str(value).strip()

def BenchmarkTest42038(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
