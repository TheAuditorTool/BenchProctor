# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest28706(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
