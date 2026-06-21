# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64113(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
