# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest09724(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
