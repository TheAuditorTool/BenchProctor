# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import urllib.request
import urllib.parse
import ssl


def normalise_input(value):
    return value.strip()

def BenchmarkTest65172(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
