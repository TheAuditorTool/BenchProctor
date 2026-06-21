# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest52289(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
