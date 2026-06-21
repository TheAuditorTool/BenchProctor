# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest71265(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
