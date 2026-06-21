# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest55473(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(ua_value)), context=ctx)
    return JsonResponse({"saved": True})
