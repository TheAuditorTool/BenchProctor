# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest31833(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
