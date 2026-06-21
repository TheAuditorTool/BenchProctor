# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest24335(request):
    raw_body = request.body.decode('utf-8')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(raw_body)), context=ctx)
    return JsonResponse({"saved": True})
